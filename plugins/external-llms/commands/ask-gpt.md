---
description: Ask OpenAI GPT. Usage: /ask-gpt <prompt> (uses gpt-4o by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask GPT

You are an interface to OpenAI's GPT models.

When the user runs this command, use the `Bash` tool to query GPT via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider openai --model gpt-4o --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
