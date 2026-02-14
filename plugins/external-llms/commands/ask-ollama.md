---
description: Ask generic local Ollama. Usage: /ask-ollama <prompt> (uses llama3 by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Ollama

You are an interface to local Ollama models.

When the user runs this command, use the `Bash` tool to query Ollama via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider ollama --model llama3 --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
