import matplotlib.pyplot as plt

# Create a 2x2 grid using subplots()
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot([1, 2, 3], [1, 4, 9])
axs[0, 0].set_title("Plot 1")

axs[0, 1].plot([1, 2, 3], [9, 4, 1])
axs[0, 1].set_title("Plot 2")

axs[1, 0].plot([1, 2, 3], [2, 2, 2])
axs[1, 0].set_title("Plot 3")

axs[1, 1].plot([1, 2, 3], [0, -1, -2])
axs[1, 1].set_title("Plot 4")

plt.tight_layout()
plt.show()
