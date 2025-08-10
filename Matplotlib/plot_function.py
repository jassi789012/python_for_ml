# plt.plot(x, y, color='color_name', linestyle='style', linewidth=value, marker='marker symbol' label = 'label name')
# plt.xlabel('label name')
# plt.ylabel('label name')
# plt.title('title name') for heading

# Values for lgend(loc = value):

# | Code | String Equivalent |
# | ---- | ----------------- |
# | `0`  | `'best'`          |
# | `1`  | `'upper right'`   |
# | `2`  | `'upper left'`    |
# | `3`  | `'lower left'`    |
# | `4`  | `'lower right'`   |
# | `5`  | `'right'`         |
# | `6`  | `'center left'`   |
# | `7`  | `'center right'`  |
# | `8`  | `'lower center'`  |
# | `9`  | `'upper center'`  |
# | `10` | `'center'`        |


import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [1000, 1500, 1200, 1800]

plt.plot(months, sales, color='blue', linestyle='--', linewidth=2, marker='o', label='2025 Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales per month')
plt.title('Monthly Sales Data Report')
plt.legend(loc='lower right')
plt.grid(color='gray', linestyle=':', linewidth=1)
plt.xlim(1, 4)
plt.ylim(0, 2000)
plt.xticks([1,2,3,4], ['M1', 'M2', 'M3', 'M4'])
plt.show() 