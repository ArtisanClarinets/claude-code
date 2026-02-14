---
description: Ask OpenAI GPT. Usage: /ask-gpt <prompt> (uses gpt-4o by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask GPT

Query OpenAI GPT.

```!
"${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py" --provider openai --model gpt-4o --prompt $ARGUMENTS
```
