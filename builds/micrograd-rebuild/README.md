# micrograd-rebuild

Backprop engine from scratch — no PyTorch.

## Goals

- Implement scalar autograd (Value class, forward/backward)
- Support basic ops: add, mul, pow, relu, tanh
- Topological sort for gradient propagation
- Train a tiny MLP on a toy dataset

## Structure

```
micrograd-rebuild/
├── engine.py      # Value, autograd graph
├── nn.py          # Neuron, Layer, MLP
├── train.py       # Training loop
└── tests/
    └── test_engine.py
```
