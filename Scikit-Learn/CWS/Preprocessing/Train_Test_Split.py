import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'StudyHours': [1, 2, 3, 4, 5],
    'TestScore': [40, 50, 60, 70, 80]
}

df = pd.DataFrame(data)

print('Data Frame:')
print(df)

X = df['StudyHours']
y = df['TestScore']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print('Training Data X:')
print(X_train)

print('Testing Data X:')
print(X_test)