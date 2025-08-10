# plt.pie(values, labels='label_list', colors='color_list', autopct='%1.1f%%')

import matplotlib.pyplot as plt

region = ['North', 'South', 'East', 'West']
revenue = [3000, 2000, 1500, 1000]

plt.pie(revenue, labels=region, autopct='%1.1f%%', colors=['gold', 'skyblue', 'lightgreen', 'coral'])
plt.title('Revenue Contribution by Region')
plt.show()