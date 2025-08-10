from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {
    'Name': ['Kamal', 'Karan', 'Kartik', 'Neha', 'Jassi', 'Jasveer'],
    'Beard': ['yes', 'no', 'yes', 'no', 'yes', 'no'],
    'Gender': ['male', 'male', 'male', 'fe-male', 'male', 'male']
}

df = pd.DataFrame(data)

le = LabelEncoder()

df['Beard_encoded'] = le.fit_transform(df['Beard'])
df['Gender_encoded'] = le.fit_transform(df['Gender'])

print(df)