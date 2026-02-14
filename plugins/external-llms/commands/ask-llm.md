---
description: Ask an external LLM provider. Usage: /ask-llm --provider <provider> --model <model> --prompt "<prompt>"
argument-hint: --provider PROVIDER --model MODEL --prompt PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask LLM

Query an external LLM provider.

```!
"${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py" $ARGUMENTS
```
