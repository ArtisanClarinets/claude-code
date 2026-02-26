---
description: Ask Anthropic. Usage: /ask-anthropic <prompt> (uses claude-3-opus-20240229 by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Anthropic

You are an interface to Anthropic's Claude models.

When the user runs this command, use the `Bash` tool to query Claude via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider anthropic --model claude-3-opus-20240229 --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
