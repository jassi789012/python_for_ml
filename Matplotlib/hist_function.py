# plt.hist(data, bins='number of bins', color='colorname', edgecolor= 'black')
import matplotlib.pyplot as plt

scores = [45, 67, 89, 92, 60, 75, 80, 55, 70, 85, 90, 95, 100]
plt.hist(scores, bins=5, color='purple', edgecolor='black')
plt.xlabel('Scores Range')
plt.ylabel('Number of Students')
plt.title('Score Distribution of Students')
plt.show()










