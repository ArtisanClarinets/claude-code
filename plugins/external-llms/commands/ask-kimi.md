---
description: Ask Moonshot AI Kimi. Usage: /ask-kimi <prompt> (uses moonshot-v1-8k by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Kimi

You are an interface to Moonshot AI's Kimi model.

When the user runs this command, use the `Bash` tool to query Kimi via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider kimi --model moonshot-v1-8k --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
