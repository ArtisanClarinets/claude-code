---
description: Ask Mistral. Usage: /ask-mistral <prompt> (uses mistral-large-latest by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Mistral

You are an interface to Mistral AI.

When the user runs this command, use the `Bash` tool to query Mistral via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider mistral --model mistral-large-latest --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
