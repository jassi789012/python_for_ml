from sklearn.neighbors import KNeighborsClassifier

X = [
    [180, 7],
    [200, 7.5],
    [250, 8],
    [300, 8.5],
    [330, 9],
    [360, 9.5]
]

y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors = 3)

model.fit(X, y)

weight = float(input('Enter the weight in grams : '))
size = float(input('Enter the size in cm : '))

predicted_marks = model.predict([[weight, size]])[0]

if predicted_marks == 1:
    print(f'This is likely to be an Orange')
else:
    print(f'This is likely to be an Apple')