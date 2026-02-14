---
description: Ask Gemini. Usage: /ask-gemini <prompt> (uses gemini-1.5-pro-latest by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Gemini

You are an interface to Google's Gemini model.

When the user runs this command, use the `Bash` tool to query Gemini via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider gemini --model gemini-1.5-pro-latest --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
