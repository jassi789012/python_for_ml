from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

def print_accuracy(prediction):

    accuracy = accuracy_score(prediction, y_test)

    print('Correct Prediction Rate Out of One : ', accuracy)

    accuracy_percentage = accuracy * 100

    print('Model Acurracy: ',accuracy_percentage)


data = {'Name': ['Aman', 'Priya', 'Rahul', 'Anjali', 'Ravi', 'Meera', 'Arjun', 'Neha', 'Imran', 'Sneha', 'Raj', 'Divya', 'Kabir', 'Simran', 'Karan', 'Pooja', 'Rakesh', 'Isha', 'Rohit', 'Deepa'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'City': ['Delhi', 'Mumbai', 'Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Bangalore', 'Delhi', 'Chennai', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 'Chennai', 'Delhi', 'Delhi', 'Bangalore'],
        'Passed': ['Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes']}

df = pd.DataFrame(data)

ll = LabelEncoder()

df['Gender_encoded'] = ll.fit_transform(df['Gender'])
df['Passed_encoded'] = ll.fit_transform(df['Passed'])

df = pd.get_dummies(df, columns=['City'], dtype=int)

df = df.drop(['Name','Gender', 'Passed'], axis=1)

X = df.drop(['Passed_encoded'], axis=1)

y = df['Passed_encoded']

# print('Values in X : \n',X)
# print('Values in y : \n',y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Using LogisticRegression Model
lr = LogisticRegression(random_state=42)

lr.fit(X_train, y_train)

prediction = lr.predict(X_test)

print('Using LogisticRegression Model : \n')
print_accuracy(prediction)
print('\n'*2)




# Using KNeighborsClassifier Model
cf = KNeighborsClassifier()

cf.fit(X_train, y_train)

prediction = cf.predict(X_test)

print('Using KNeighborsClassifier Model : \n')
print_accuracy(prediction)
print('\n'*2)






# Using DecisionTreeClassifier
dtc = DecisionTreeClassifier()

dtc.fit(X_train, y_train)

prediction = dtc.predict(X_test)

print('Using DecisionTreeClassifier Model : \n')
print_accuracy(prediction)
print('\n'*2)




