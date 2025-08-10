import pandas as pd

data = {
    'Name': ['Kamal', 'Karan', 'Kartik', 'Neha', 'Jassi', 'Jasveer'],
    'Beard': ['yes', 'no', 'yes', 'no', 'yes', 'no'],
    'Gender': ['male', 'male', 'male', 'fe-male', 'male', 'male'],
    'City': ['Pathankot', 'Mirpur', 'Tung', 'Singhowal', 'Dagan', 'Swar']
}

df = pd.DataFrame(data)
df_labeled = df.copy()
df_City_Encoded = pd.get_dummies(df_labeled, columns=['City'], dtype=int)
print(df_City_Encoded)