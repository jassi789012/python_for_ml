import numpy as np

arr_2d = np.array([[1,2],[3,4]])

arr_2d_new = np.insert(arr_2d, 1, [5,6], axis=0)

print(arr_2d)
print(arr_2d_new)