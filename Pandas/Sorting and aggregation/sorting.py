# sorting data of 1 column
# df.sort_values(by='Column_name', True/False, inplace=True)
# True for asend order / False for desend order

import pandas as pd

data = {
    'Name' : ['Arun', 'Varun', 'Karun'],
    'Age' : [28, 34, 22],
    'Salary' : [10000, 20000, 30000]
}

df = pd.DataFrame(data)

df.sort_values(by='Age', ascending=False, inplace=True)
print(df)