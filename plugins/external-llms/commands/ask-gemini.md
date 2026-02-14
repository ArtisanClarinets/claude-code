---
description: Ask Gemini. Usage: /ask-gemini <prompt> (uses gemini-1.5-pro-latest by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Gemini

Query Gemini.

```!
"${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py" --provider gemini --model gemini-1.5-pro-latest --prompt "$ARGUMENTS"
```
