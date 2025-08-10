from sklearn.tree import DecisionTreeClassifier

X = [
    [7, 2], #Apple
    [8, 3], #Apple
    [9, 8], #Orange
    [10, 9] #Orange
]

y = [0, 0, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, y)

size = float(input('Enter the size : '))
color_shade = float(input('Enter the Color Shade : '))

predicted_marks = model.predict([[size, color_shade]])[0]

if predicted_marks == 1:
    print(f'This is likely to be an Orange')
else:
    print(f'This is likely to be an Apple')