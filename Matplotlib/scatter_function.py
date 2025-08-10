# plt.scatter(x, y, color='color_name', marker='marker_style', label='label_name')

import matplotlib.pyplot as plt

hours_studed = [1,2,3,4,5,6,7,8]

exam_score = [50,55,60,65,70,75,80,85]

plt.scatter(hours_studed, exam_score, color='green', marker='o', label='Student data')
plt.xlabel('Hours Studed')
plt.ylabel('Exam Score')

plt.title('Relationship between Hours studed and Exam score')
plt.legend()
plt.grid(True)

plt.show()
