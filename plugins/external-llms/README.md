# External LLMs Plugin

This plugin allows Claude Code to interact with other LLM providers, including OpenAI, Google Gemini, Ollama (local), Moonshot AI (Kimi), OpenRouter, and Generic OpenAI-compatible endpoints (like LM Studio).

## Setup

1.  **Ensure Python 3 is installed.** This plugin uses a Python script to query APIs.
2.  **Set Environment Variables.** Add the following to your shell profile (e.g., `~/.bashrc`, `~/.zshrc`) or `.env` file if supported by your setup:

    ```bash
    export OPENAI_API_KEY="sk-..."
    export GEMINI_API_KEY="AIza..."
    export KIMI_API_KEY="sk-..."
    export OPENROUTER_API_KEY="sk-or-..."
    export STUDIO_API_KEY="lm-studio" # Optional for local generic
    export STUDIO_BASE_URL="http://localhost:1234" # Optional for local generic
    export OLLAMA_BASE_URL="http://localhost:11434" # Optional, default is localhost
    ```

## Usage

### Commands

You can use the following commands directly:

-   `/ask-llm --provider <provider> --model <model> --prompt "<prompt>"`: Generic query.
-   `/ask-gemini <prompt>`: Ask Google Gemini (default: gemini-1.5-pro-latest).
-   `/ask-gpt <prompt>`: Ask OpenAI GPT (default: gpt-4o).
-   `/ask-ollama <prompt>`: Ask local Ollama (default: llama3).
-   `/ask-kimi <prompt>`: Ask Moonshot AI Kimi (default: moonshot-v1-8k).
-   `/ask-openrouter <prompt>`: Ask OpenRouter (default: openai/gpt-3.5-turbo).

### Agents

You can also ask Claude to consult these agents:

-   "Ask Gemini to explain this code."
-   "Ask GPT to rewrite this function."
-   "Use the Ollama agent to check this locally."

The available agents are: `gemini`, `gpt`, `ollama`, `kimi`, `openrouter`, `studio`.

## Supported Providers

-   **openai**: OpenAI API (GPT-4, GPT-3.5, etc.)
-   **gemini**: Google Generative AI (Gemini Pro, Flash, etc.)
-   **ollama**: Local LLM runner (Llama 3, Mistral, etc.)
-   **kimi**: Moonshot AI
-   **openrouter**: OpenRouter Aggregator
-   **studio**: Generic OpenAI-compatible endpoint (e.g. LM Studio)

## Troubleshooting

If commands fail:
1.  Check your API keys are set correctly in the environment where `claude` is running.
2.  Ensure Python 3 is in your PATH.
3.  Check connectivity (e.g., for Ollama, ensure the server is running).
