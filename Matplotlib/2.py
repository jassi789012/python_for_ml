import matplotlib.pyplot as plt

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

y = [10, 15, 7, 20, 12]

plt.plot(x, y)

plt.title('Weekly Sales this week!')

plt.xlabel('Day of the Week') 

plt.ylabel('Sales per Day')

plt.show()