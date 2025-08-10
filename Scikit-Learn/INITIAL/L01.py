from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
iris = load_iris()

# Print the description (the "datasheet")
# print(iris.DESCR)

# Access the feature data
X = iris.data
# print("Shape of feature data (X):", X.shape)

# Access the target labels
y = iris.target
# print("Shape of target data (y):", y.shape)


# print(iris.data)
print(iris.target)


# You can combine the data and targets into a pandas DataFrame for easier viewing
df = pd.DataFrame(data=X, columns=iris.feature_names)
df['target'] = y
# print("\nFirst 5 rows of the combined DataFrame:")
# print(df.head())


# model1 = LinearRegression()
# model1.fit(X, y)

# print(model1.predict(X))



model2 = KNeighborsRegressor()
model2.fit(X, y)

print(model2.predict(X))


plt.scatter(model2.predict(X), y, color='green', marker='o', label='Data Prediction Acurracy')
plt.xlabel('Predicted Data')
plt.ylabel('Original Data')

plt.title('Predicted and Original Data')
plt.legend()
plt.grid(True)

plt.show()