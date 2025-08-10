# slicing

# array[start:stop:step]

# stop is excluded for ex if : stop = n then stop will be seen as n - 1


import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[1:5])
print(arr[:4])
print(arr[::2])
print(arr[::-1])

