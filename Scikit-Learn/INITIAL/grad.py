w = 0  # initial guess
learning_rate = 0.1
iterations = 20

for i in range(iterations):
    grad = 2 * (w - 3)          # calculate gradient
    w = w - learning_rate * grad  # update w
    print(f"Iteration {i+1}: w = {w:.4f}, f(w) = {(w - 3)**2:.4f}")
