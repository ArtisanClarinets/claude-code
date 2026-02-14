---
description: Ask Moonshot AI Kimi. Usage: /ask-kimi <prompt> (uses moonshot-v1-8k by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Kimi

Query Kimi.

```!
"${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py" --provider kimi --model moonshot-v1-8k --prompt $ARGUMENTS
```
