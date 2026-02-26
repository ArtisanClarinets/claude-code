---
description: Ask Groq. Usage: /ask-groq <prompt> (uses llama3-70b-8192 by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Groq

You are an interface to Groq.

When the user runs this command, use the `Bash` tool to query Groq via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider groq --model llama3-70b-8192 --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
