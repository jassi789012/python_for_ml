import time

prices = [i for i in range(0,100000000)]

discount = 10

final_prices = []

start = time.time()
for price in prices:
    final_prices.append(price-price*(discount/100))

# print(final_prices)

end = time.time() - start
print(end)

import numpy as np

np_prices = np.array(prices)

np_start = time.time()
np_final_prices = np_prices - (np_prices * discount / 100)

# print(np_final_prices)
np_end = time.time() - np_start
print(np_end)