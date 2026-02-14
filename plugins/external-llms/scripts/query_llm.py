import argparse
import os
import json
import sys
import urllib.request
import urllib.error

def query_openai_compatible(api_key, base_url, model, prompt):
    url = base_url
    if not url.endswith("/chat/completions"):
         # Try to append if not present, but respect full URLs
         if not url.endswith("/v1"):
             url = f"{url}/v1/chat/completions"
         else:
             url = f"{url}/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
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
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
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
    url = f"{base_url}/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            result = json.load(response)
            if 'response' in result:
                return result['response']
            return "Error: No response content found."
    except urllib.error.HTTPError as e:
        return f"HTTP Error: {e.code} - {e.read().decode('utf-8')}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Query external LLM providers.")
    parser.add_argument("--provider", required=True, choices=["openai", "gemini", "ollama", "kimi", "openrouter", "studio"], help="LLM Provider")
    parser.add_argument("--model", required=True, help="Model name")
    parser.add_argument("--prompt", required=True, help="Prompt text")

    args = parser.parse_args()

    if args.provider == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("Error: OPENAI_API_KEY environment variable not set.")
            sys.exit(1)
        print(query_openai_compatible(api_key, "https://api.openai.com", args.model, args.prompt))

    elif args.provider == "gemini":
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("Error: GEMINI_API_KEY environment variable not set.")
            sys.exit(1)
        print(query_gemini(api_key, args.model, args.prompt))

    elif args.provider == "ollama":
        base_url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
        print(query_ollama(base_url, args.model, args.prompt))

    elif args.provider == "kimi":
        api_key = os.environ.get("KIMI_API_KEY")
        if not api_key:
            print("Error: KIMI_API_KEY environment variable not set.")
            sys.exit(1)
        print(query_openai_compatible(api_key, "https://api.moonshot.cn", args.model, args.prompt))

    elif args.provider == "openrouter":
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            print("Error: OPENROUTER_API_KEY environment variable not set.")
            sys.exit(1)
        print(query_openai_compatible(api_key, "https://openrouter.ai/api", args.model, args.prompt))

    elif args.provider == "studio":
        # Assuming generic OpenAI compatible endpoint, e.g. LM Studio
        api_key = os.environ.get("STUDIO_API_KEY", "lm-studio") # Default dummy key for local
        base_url = os.environ.get("STUDIO_BASE_URL", "http://localhost:1234")
        print(query_openai_compatible(api_key, base_url, args.model, args.prompt))

if __name__ == "__main__":
    main()
