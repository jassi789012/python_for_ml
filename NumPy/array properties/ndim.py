import numpy as np

arr_1d = np.array([10, 20, 30])

arr_2d = np.array([[10, 20, 30],
                   [40, 50 ,60]])


arr_3d = np.array([[[1,2,3]]])


# number of dimention in an array

print(arr_1d.ndim)

print(arr_2d.ndim)

print(arr_3d.ndim)