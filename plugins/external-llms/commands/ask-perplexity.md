---
description: Ask Perplexity. Usage: /ask-perplexity <prompt> (uses llama-3-sonar-large-32k-online by default)
argument-hint: PROMPT
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py:*)"]
---

# Ask Perplexity

You are an interface to Perplexity AI.

When the user runs this command, use the `Bash` tool to query Perplexity via the `query_llm.py` script.
Construct the command like this:
`${CLAUDE_PLUGIN_ROOT}/scripts/query_llm.py --provider perplexity --model llama-3-sonar-large-32k-online --prompt "USER_PROMPT"`

Replace `USER_PROMPT` with the content of $ARGUMENTS.
Ensure you quote the prompt to avoid shell issues.
