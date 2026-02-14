---
description: Ask OpenRouter. Usage: /ask-openrouter <prompt> (uses openai/gpt-3.5-turbo by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask OpenRouter

You are an interface to OpenRouter.

When the user runs this command, use the `Bash` tool to query OpenRouter via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider openrouter --model openai/gpt-3.5-turbo --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
