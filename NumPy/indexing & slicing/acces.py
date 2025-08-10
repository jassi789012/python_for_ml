# arrray[index] for one dimentional array

# array[row, column] for two dimentional array

# negative indexing is also available


import numpy as np


arr = np.array([10, 20, 30, 40])


print(arr[0])
print(arr[2])

arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])


print(arr_2d[0, 0])
print(arr_2d[1, 1])
print(arr_2d[2, 2])


