import matplotlib.pyplot as plt

# Create 4 plots in a 2x2 grid using subplot()
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Plot 1")

plt.subplot(2, 2, 2)
plt.plot([1, 2, 3], [9, 4, 1])
plt.title("Plot 2")

plt.subplot(2, 2, 3)
plt.plot([1, 2, 3], [2, 2, 2])
plt.title("Plot 3")

plt.subplot(2, 2, 4)
plt.plot([1, 2, 3], [0, -1, -2])
plt.title("Plot 4")

plt.tight_layout()
plt.show()
