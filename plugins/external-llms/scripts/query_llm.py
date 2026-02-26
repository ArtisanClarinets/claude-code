import argparse
import os
import json
import sys
import urllib.request
import urllib.error
import urllib.parse

def validate_url(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        raise ValueError(f"Invalid URL scheme: {parsed.scheme}. Only 'http' and 'https' are allowed.")
    return url

def query_openai_compatible(api_key, base_url, model, prompt):
    base_url = base_url.strip()
    validate_url(base_url)

    url = base_url
    if not url.endswith("/chat/completions"):
         # Try to append if not present, but respect full URLs
         if not url.endswith("/v1"):
             url = f"{url}/v1/chat/completions"
         else:
             url = f"{url}/chat/completions"

    # Explicitly check scheme again just before usage for security audit compliance
    if not url.startswith("https://") and not url.startswith("http://"):
        raise ValueError("Only HTTP(S) URLs are allowed.")

    if '\n' in api_key or '\r' in api_key:
        return "Error: API Key contains newline characters."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key.strip()}"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
        # nosemgrep
        with urllib.request.urlopen(req) as response:
            result = json.load(response)
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
            return "Error: No response content found."
    except urllib.error.HTTPError as e:
        return f"HTTP Error: {e.code} - {e.read().decode('utf-8')}"
    except Exception as e:
        return f"Error: {str(e)}"

def query_gemini(api_key, model, prompt):
    api_key = api_key.strip()
    if '\n' in api_key or '\r' in api_key:
        return "Error: API Key contains newline characters."

    encoded_model = urllib.parse.quote(model)
    encoded_key = urllib.parse.quote(api_key)

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{encoded_model}:generateContent?key={encoded_key}"

    # Explicitly check scheme just before usage for security audit compliance (redundant for hardcoded string but good practice)
    if not url.startswith("https://"):
         raise ValueError("Only HTTPS URLs are allowed.")

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
        # nosemgrep
        with urllib.request.urlopen(req) as response:
            result = json.load(response)
            if 'candidates' in result and len(result['candidates']) > 0:
                content = result['candidates'][0]['content']['parts'][0]['text']
                return content
            return "Error: No response content found."
    except urllib.error.HTTPError as e:
        return f"HTTP Error: {e.code} - {e.read().decode('utf-8')}"
    except Exception as e:
        return f"Error: {str(e)}"

def query_ollama(base_url, model, prompt):
    base_url = base_url.strip()
    validate_url(base_url)

    url = f"{base_url}/api/generate"

    # Explicitly check scheme just before usage for security audit compliance
    if not url.startswith("https://") and not url.startswith("http://"):
        raise ValueError("Only HTTP(S) URLs are allowed.")

    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
        # nosemgrep
        with urllib.request.urlopen(req) as response:
            result = json.load(response)
            if 'response' in result:
                return result['response']
            return "Error: No response content found."
    except urllib.error.HTTPError as e:
        return f"HTTP Error: {e.code} - {e.read().decode('utf-8')}"
    except Exception as e:
        return f"Error: {str(e)}"

def query_anthropic(api_key, model, prompt):
    api_key = api_key.strip()
    if '\n' in api_key or '\r' in api_key:
        return "Error: API Key contains newline characters."

    url = "https://api.anthropic.com/v1/messages"

    # Explicitly check scheme just before usage for security audit compliance
    if not url.startswith("https://"):
         raise ValueError("Only HTTPS URLs are allowed.")

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    data = {
        "model": model,
        "max_tokens": 4096,
        "messages": [{"role": "user", "content": prompt}]
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
        # nosemgrep
        with urllib.request.urlopen(req) as response:
            result = json.load(response)
            if 'content' in result and len(result['content']) > 0:
                return result['content'][0]['text']
            return "Error: No response content found."
    except urllib.error.HTTPError as e:
        return f"HTTP Error: {e.code} - {e.read().decode('utf-8')}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Query external LLM providers.")
    parser.add_argument("--provider", required=True, choices=[
        "openai", "gemini", "ollama", "kimi", "openrouter", "studio",
        "anthropic", "mistral", "groq", "perplexity", "deepseek"
    ], help="LLM Provider")
    parser.add_argument("--model", required=True, help="Model name")
    parser.add_argument("--prompt", required=True, nargs='+', help="Prompt text")

    args = parser.parse_args()
    prompt_text = " ".join(args.prompt)

    try:
        if args.provider == "openai":
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                print("Error: OPENAI_API_KEY environment variable not set.")
                sys.exit(1)
            print(query_openai_compatible(api_key, "https://api.openai.com", args.model, prompt_text))

        elif args.provider == "gemini":
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                print("Error: GEMINI_API_KEY environment variable not set.")
                sys.exit(1)
            print(query_gemini(api_key, args.model, prompt_text))

        elif args.provider == "ollama":
            base_url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
            print(query_ollama(base_url, args.model, prompt_text))

        elif args.provider == "kimi":
            api_key = os.environ.get("KIMI_API_KEY")
            if not api_key:
                print("Error: KIMI_API_KEY environment variable not set.")
                sys.exit(1)
            print(query_openai_compatible(api_key, "https://api.moonshot.cn", args.model, prompt_text))

        elif args.provider == "openrouter":
            api_key = os.environ.get("OPENROUTER_API_KEY")
            if not api_key:
                print("Error: OPENROUTER_API_KEY environment variable not set.")
                sys.exit(1)
            print(query_openai_compatible(api_key, "https://openrouter.ai/api", args.model, prompt_text))

        elif args.provider == "studio":
            api_key = os.environ.get("STUDIO_API_KEY", "lm-studio")
            base_url = os.environ.get("STUDIO_BASE_URL", "http://localhost:1234")
            print(query_openai_compatible(api_key, base_url, args.model, prompt_text))

        elif args.provider == "anthropic":
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not api_key:
                print("Error: ANTHROPIC_API_KEY environment variable not set.")
                sys.exit(1)
            print(query_anthropic(api_key, args.model, prompt_text))

        elif args.provider == "mistral":
            api_key = os.environ.get("MISTRAL_API_KEY")
            if not api_key:
                print("Error: MISTRAL_API_KEY environment variable not set.")
                sys.exit(1)
            print(query_openai_compatible(api_key, "https://api.mistral.ai", args.model, prompt_text))

        elif args.provider == "groq":
            api_key = os.environ.get("GROQ_API_KEY")
            if not api_key:
                print("Error: GROQ_API_KEY environment variable not set.")
                sys.exit(1)
            print(query_openai_compatible(api_key, "https://api.groq.com/openai", args.model, prompt_text))

        elif args.provider == "perplexity":
            api_key = os.environ.get("PERPLEXITY_API_KEY")
            if not api_key:
                print("Error: PERPLEXITY_API_KEY environment variable not set.")
                sys.exit(1)
            print(query_openai_compatible(api_key, "https://api.perplexity.ai", args.model, prompt_text))

        elif args.provider == "deepseek":
            api_key = os.environ.get("DEEPSEEK_API_KEY")
            if not api_key:
                print("Error: DEEPSEEK_API_KEY environment variable not set.")
                sys.exit(1)
            print(query_openai_compatible(api_key, "https://api.deepseek.com", args.model, prompt_text))

    except ValueError as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
