# plt.bar(x, height, color='color_name', width=value, label='label name')
# use barh for horizontal bar chart

import matplotlib.pyplot as plt

product = ['A', 'B', 'C', 'D']
sales = [1000, 1500, 800, 1200]

plt.bar(product, sales, color='orange', label='Sales 2025')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product Sales Comparison')
plt.legend()
plt.show()