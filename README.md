> ⚠️ Work in progress — sections will be added as the work progresses.

# AI Engineering from Scratch

Building the full stack from first principles — backprop, transformers,
LLM internals, agent loops, and multi-agent coordination — to own what
I currently ship in production.

## Why this exists

I've been building agentic systems professionally (FastAPI, LangChain,
Anthropic SDK, pgvector) but hitting optimization walls I can't reason
through because I don't own the internals. This repo documents fixing
that — going from API-level to mechanism-level understanding, so I can
optimize what I build, read research papers, and contribute to the field
rather than just consume from it.

## What I'm building toward

- Student researcher in multi-agent AI systems at NTU
- Research or engineering role at a frontier lab

---

## Curriculum

Adapted from [AI Engineering from Scratch](https://aiengineeringfromscratch.com)
by Rohit Ghumare — a free, open-source curriculum spanning 503 lessons
across 20 phases. This version combines the curriculum's structure with
targeted YouTube resources, covering the theory spine relevant to agentic AI.

Original source: https://github.com/rohitg00/ai-engineering-from-scratch

| Phase | Focus | Status |
|---|---|---|
| Math Foundations | Gradient descent, chain rule, autodiff | ✅ |
| Deep Learning | Backprop, optimizers, PyTorch | ⬜ |
| Transformers | Self-attention, multi-head attention, GPT architecture | ⬜ |
| LLMs from Scratch | Tokenizers, pre-training, RLHF, DPO | ⬜ |
| Application Layer | Evals, RAG optimization, LoRA, structured outputs | ⬜ |
| Agent Engineering | Agent loop, memory, tool dispatch | ⬜ |
| Multi-Agent Systems | Coordination, hierarchical swarms, DAG orchestration | ⬜ |

---

## Major builds

| Build | Description |
|---|---|
| [micrograd-rebuild](./builds/micrograd-rebuild/) | Backprop engine from scratch, no PyTorch |
| [attention-numpy](./builds/attention-numpy/) | Scaled dot-product + multi-head attention in raw NumPy, with test cases |
| [llm-eval-harness](./builds/llm-eval-harness/) | Reproducible eval suite for LLM-powered agents — 30 test cases, pass/fail scoring |
| [agent-from-scratch](./builds/agent-from-scratch/) | Full agent loop using Anthropic SDK only, no LangChain — tool dispatch, memory, retry logic |
| [multi-agent-coordination](./builds/multi-agent-coordination/) | Two-agent orchestration system |

---

## Lessons

Each lesson has a `notes.md` covering: what I watched, what I built, the
key insight, what I got wrong, and how it connects to systems I've
already shipped.

- [Lesson 1 — Foundations](./lesson-1-foundations/notes.md) — Math foundations + Deep learning & backprop
- [Lesson 2 — Architectures](./lesson-2-architectures/notes.md) — Transformers, LLM internals, application layer, agents, multi-agent

---

## Papers (reading in parallel)

- [ ] Attention is All You Need — Vaswani et al., 2017
- [ ] ReAct: Synergizing Reasoning and Acting — Yao et al., 2022
- [ ] Reflexion: Language Agents with Verbal Reinforcement — Shinn et al., 2023
- [ ] A Survey on Large Language Model based Autonomous Agents — Wang et al., 2023