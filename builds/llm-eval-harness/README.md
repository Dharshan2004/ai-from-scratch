# llm-eval-harness

Reproducible eval suite for LLM-powered agents — 30 test cases, pass/fail scoring.

## Goals

- Define 30 agent test cases with expected outcomes
- Run evals against an agent implementation
- Score pass/fail with reproducible results

## Structure

```
llm-eval-harness/
├── harness.py
├── cases/
│   └── test_cases.json
└── tests/
    └── test_harness.py
```
