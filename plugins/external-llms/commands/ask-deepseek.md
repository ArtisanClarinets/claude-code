---
description: Ask DeepSeek. Usage: /ask-deepseek <prompt> (uses deepseek-coder by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask DeepSeek

You are an interface to DeepSeek.

When the user runs this command, use the `Bash` tool to query DeepSeek via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider deepseek --model deepseek-coder --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
