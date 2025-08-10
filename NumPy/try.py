import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load data
df = pd.read_csv('Churn.csv')

# Preprocessing
X = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))
y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Print a sample of the target
print(y_train.head())

# Build model
model = Sequential()
model.add(Dense(units=32, activation='relu', input_dim=len(X_train.columns)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

# Compile model (corrected metrics)
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Fit model
model.fit(X_train, y_train, epochs=10, verbose=1)

# Predict and evaluate
preds = model.predict(X_test)
preds = [1 if p > 0.5 else 0 for p in preds]

print("Accuracy on test set:", accuracy_score(y_test, preds))

model.fit(X_train, y_train, epochs=200, batch_size=32)

y_hat = model.predict(X_test)
y_hat = [0 if val < 0.5 else 1 for val in y_hat]

accuracy_score(y_test, y_hat)