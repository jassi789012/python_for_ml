import pandas as pd

data = {
    'Name': ['Pavan', 'Kapil', 'Lalit', 'Ishan', 'Om'],
    'Age': [25, None, 44, 23, None],
    'Salary': [50000, 60000, 70000, None, None]
}

df = pd.DataFrame(data)
# print(df)

print(df.isnull().sum())

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print(df.isnull().sum())
print(df)