from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5]]

y = [0, 0, 1, 1, 1]

model = LogisticRegression()

model.fit(X, y)

hours = float(input("Enter how many hours you Studied : "))

predicted_marks = model.predict([[hours]])[0]

if predicted_marks == 1:
    print(f'You are likely to pass')
else:
    print(f'You are likely to fail')