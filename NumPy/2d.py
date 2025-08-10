import numpy as np

_2d_array = np.array([[10,20,30,40],[50,60,70,80]])

print(_2d_array)



# np.zeros(shape)
zeros_array = np.zeros(3)

print(zeros_array)


# np.ones(shape)
ones_array = np.ones((2, 3))

print(ones_array)


# np.full(shape, value)

filled_array = np.full((3,2),25)

print(filled_array)


# sequence of numbers

arr = np.arange(1, 10, 2)

print(arr)


# identity matrix

identity_matrix = np.eye(3)

print(identity_matrix)