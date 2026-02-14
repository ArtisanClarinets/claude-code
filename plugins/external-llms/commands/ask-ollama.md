---
description: Ask generic local Ollama. Usage: /ask-ollama <prompt> (uses llama3 by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Ollama

Query Ollama locally.

```!
"${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py" --provider ollama --model llama3 --prompt $ARGUMENTS
```
