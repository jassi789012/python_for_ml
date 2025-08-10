from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]

y = [40, 50, 65, 75, 90]

model = LinearRegression()

model.fit(X, y)

hours = float(input("Enter how many hours you Studied : "))

predicted_marks = model.predict([[hours]])[0]

print(predicted_marks)