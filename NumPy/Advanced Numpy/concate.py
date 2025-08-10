# np.concatenate((array1, array2), axis=0)

import numpy as np

arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])

new_arr = np.concatenate((arr1, arr2))

print(new_arr)