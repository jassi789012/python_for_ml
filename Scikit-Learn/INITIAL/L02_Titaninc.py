import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

# fetch_openml('_dataset_name_', version='_version_of_dataset_', as_frame='True for pandas dataset False for numpy array in return')
df = fetch_openml('titanic', version=1, as_frame=True)['data']

# print(df.isnull().sum())

null_val_perc = (df.isnull().sum())/(len(df))*(100)


# plt.figure(figsize= (12,8))
# plt.bar(null_val_perc.index, null_val_perc.values, color='orange', label='Null Values Percentage')
# plt.xlabel('Indexes name')
# plt.ylabel('Values in Percentage')
# plt.title('Null Values Percentage')
# plt.legend()
# plt.grid()
# plt.show()

# print(df.shape)
df.drop(['body'], axis = 1, inplace = True)
# print(df.shape)

# print(f'Number of impute values in age column {df.age.isnull().sum()}')

imp = SimpleImputer(strategy='mean')
df['age'] = imp.fit_transform(df[['age']])

# print(f'Number of impute values in age column {df.age.isnull().sum()}')

def get_parameters(df):
    parameters = {}
    for col in df.columns[df.isnull().any()]:
        
        if df[col].dtype == 'float64' or df[col].dtype == 'int64' or df[col].dtype == 'int32':
            strategy = 'mean'
        else:
            strategy = 'most_frequent'
        
        parameters[col] = {'strategy': strategy}
    return parameters

# print(get_parameters(df))

parameters = get_parameters(df)

for col, param in parameters.items():
    imp = SimpleImputer(strategy=param['strategy'])
    df[[col]] = imp.fit_transform(df[[col]])



df['family'] = df['sibsp'] + df['parch']
df['travelled_alone'] = (df['family'] == 0).astype(int)

# print(df['travelled_alone'])

encoder = OneHotEncoder(sparse_output=False)  # correct keyword for newer versions
sex_encoded = encoder.fit_transform(df[['sex']])
df[['female', 'male']] = sex_encoded
df['sex'] = df['male']


num_cols = df.select_dtypes(include=['int64', 'float64', 'int32']).columns
print(num_cols)

ss = StandardScaler()
# df[num_cols] = ss.fit_transform(df[num_cols])
# print(df[num_cols].describe())

mm = MinMaxScaler()
df[num_cols] = mm.fit_transform(df[num_cols])
# print(df[num_cols].describe())