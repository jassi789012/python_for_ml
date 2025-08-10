import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# ss = StandardScaler()
# X_scaled = ss.fit_transform()

# ms = MinMaxScaler()
# X_scaled = ms.fit_transform()

data = {
    'StudyHours': [1, 2, 3, 4, 5],
    'TestScore': [40, 50, 60, 70, 80]
}

df = pd.DataFrame(data)

# ss = StandardScaler()

# df_encode = ss.fit_transform(df)

# print(pd.DataFrame(df_encode, columns=['StudyHours', 'TestScore']))

ms = MinMaxScaler()

df_encoded = ms.fit_transform(df)

print(pd.DataFrame(df_encoded, columns=['StudyHours', 'TestScore']))

