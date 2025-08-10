# savefig('filename.extension', dpi = value, bbox_inches = 'tight')

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [20, 30, 15, 73, 11]

plt.plot(x, y)
# plt.show()

plt.savefig('1py.png', dpi = 300, bbox_inches = 'tight')