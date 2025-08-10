# import numpy as np

# x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# y = np.array([0, 1, 1, 1])

# w = np.array([1, 1])

# b = -0.5

# def activation(z):
#     if z >= 0:
#         return 1
#     else:
#         return 0

# pred = []
# for a in x:
#     y_hat = np.dot(a, w) + b
#     pred.append(activation(y_hat))

# print(pred)


import numpy as np

X = np.array([[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]])
Y = np.array([0, 1, 1, 1, 1, 1, 1 ,1])

w = np.random.rand(3)
b = np.random.rand(1)
learning_rate = 0.1

def activation(z):
    return 1 if z >= 0 else 0

epoch = 0
while True:
    epoch += 1
    errors = 0
    for x, y_true in zip(X, Y):
        z = np.dot(w, x) + b
        y_pred = activation(z)
        error = y_true - y_pred
        if error != 0:
            w += learning_rate * error * x
            b += learning_rate * error
            errors += 1
    print(f"Epoch {epoch}, errors: {errors}")
    if errors == 0:
        print(f'w = {w}')
        print(f'b = {b}')
        print("Training complete!")
        break
