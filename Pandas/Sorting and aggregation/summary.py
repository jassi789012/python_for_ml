# df['Column Name'].mean()
# df['Column Name'].max()
# df['Column Name'].min()
# df['Column Name'].sum()

import pandas as pd

data = {
    'Name' : ['Arun', 'Varun', 'Karun'],
    'Age' : [28, 34, 22],
    'Salary' : [10000, 20000, 30000]
}

df = pd.DataFrame(data)

average_salary = df['Salary'].mean()

print(average_salary)