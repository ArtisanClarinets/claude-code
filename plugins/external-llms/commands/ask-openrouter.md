---
description: Ask OpenRouter. Usage: /ask-openrouter <prompt> (uses openai/gpt-3.5-turbo by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask OpenRouter

Query OpenRouter.

```!
"${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py" --provider openrouter --model openai/gpt-3.5-turbo --prompt $ARGUMENTS
```
