# np.insert(array, index, value, axis=None)
# axis in one d = None
# axis in 2 d :-
    # 0 for row wise
    # 1 for column wise

import numpy as np

arr = np.array([10,20,30,40,50,60])

new_array = np.insert(arr, 2, 100)

print(new_array)