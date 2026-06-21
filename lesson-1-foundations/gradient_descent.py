import numpy as np

# 1. Generate toy data
# True relationship: y = 2x + 1 (plus some noise)
np.random.seed(67)
X = np.random.randn(100)
y = 2 * X + 1 + np.random.randn(100) * 0.2

# 2. Initialise parameters
w = 0.0
b = 0.0
lr = 0.01
epochs = 10000

# 3. Training loop
for epoch in range(epochs):
    # Forward pass: compute predictions
    y_pred = w * X + b

    # Compute MSE loss
    loss = np.mean((y_pred - y) ** 2)

    # Compute gradients — derive these yourself
    dw = 2 * np.mean((y_pred - y) * X)
    db = 2 * np.mean(y_pred - y)

    # Step size
    w_step = lr * dw
    b_step = lr * db

    if abs(w_step) < 0.00001 or abs(b_step) < 0.00001: # min step size of 0.00001
        break

    # Update parameters
    w = w - w_step
    b = b - b_step

    if epoch % 100 == 0:
        print(f"Epoch {epoch} | Loss: {loss:.4f} | w: {w:.4f} | b: {b:.4f}")

print(f"\nFinal: w={w:.4f} (true: 2.0), b={b:.4f} (true: 1.0)")