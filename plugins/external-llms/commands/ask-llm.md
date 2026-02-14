---
description: Ask an external LLM provider. Usage: /ask-llm --provider <provider> --model <model> --prompt "<prompt>"
argument-hint: --provider PROVIDER --model MODEL --prompt PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask LLM

You are an interface to external LLM providers.

When the user runs this command, use the `Bash` tool to query the provider via the `query_llm.py` script.
Construct the command as follows:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py $ARGUMENTS`

Ensure you pass the arguments correctly.
