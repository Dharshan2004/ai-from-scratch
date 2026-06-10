# agent-from-scratch

Full agent loop using Anthropic SDK only — no LangChain. Tool dispatch, memory, retry logic.

## Goals

- Agent loop: observe → think → act → observe
- Tool dispatch with schema validation
- Conversation memory management
- Retry logic for transient failures

## Structure

```
agent-from-scratch/
├── agent.py
├── tools/
│   └── __init__.py
├── memory.py
└── tests/
    └── test_agent.py
```
