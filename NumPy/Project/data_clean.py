# importing libraries
import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv('Project/Indian_employees_data.csv')

# print shape before cleaning
print("Before cleaning:", df.shape)

# checking missing values (optional but informative)
print("Missing values before handling:")
print(df.isnull().sum())

# replacing inf and -inf with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# fill NaN in 'Salary' with its mean
if 'Salary' in df.columns:
    df['Salary'] = df['Salary'].astype(float)
    df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# fill NaN in 'Performance Rating' with its median
if 'Performance Rating' in df.columns:
    df['Performance Rating'] = df['Performance Rating'].astype(float)
    df['Performance Rating'].fillna(df['Performance Rating'].median(), inplace=True)

# fill remaining NaNs in numeric columns with their respective means
numeric_means = df.select_dtypes(include=[np.number]).mean()
df.fillna(numeric_means, inplace=True)

# replacing negative salaries with mean salary
if 'Salary' in df.columns:
    mean_salary = df['Salary'].mean()
    df['Salary'] = np.where(df['Salary'] < 0, mean_salary, df['Salary'])

# removing outliers from Salary using the 3-sigma rule
salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# filter the dataframe
df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

# print shape after cleaning
print("After cleaning:", df.shape)

# saving the cleaned dataset
df.to_csv('Cleaned Data.csv', index=False)

print('✅ Data is Cleaned and Saved as "Cleaned Data.csv"')
