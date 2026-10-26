import numpy as np 
import matplotlib.pyplot as plt

# 1. Training data
x = np.array([1, 2, 3],dtype=float)
y = np.array([3, 5, 7],dtype=float)

# 2. Initialize parameters
w = 1.0
b = 0.0

# 3. Set training configuration
learning_rate = 0.1
epochs = 100

loss_history = []

for epoch in range(epochs):
  
  # Step A: Predict
  y_pred= w * x + b
  
  # Step B: Calculate errors and loss
  errors = y_pred - y
  MSE = np.mean(errors ** 2)
  loss_history.append(MSE)
  
  # Step C: Calculate gradients
  dw = (2/3)* np.sum(x * errors)
  db = (2/3)* np.sum(errors)
  
  # Step D: Update parameters
  w = w - learning_rate * dw
  b = b - learning_rate * db
  
  print(f"Epoch {epoch:3d} | MSE: {MSE:.4f} | w: {w:.4f} | b: {b:.4f}" )
  
print("\nFinal parameters:", w, b)
print("Final predictions:", w * x + b)

plt.plot(loss_history)
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")
plt.title("Gradient Descent Learning Curve")
plt.grid(True)
plt.savefig("loss.png")