# pd.merge(df1, df2, on='Column_Name', how='type of join')

import pandas as pd

df_customer = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
})

df_order = pd.DataFrame({
    'CustomerID': [1, 2, 2, 3],
    'OrderAmount': [250, 150, 200, 300]
})

merged_df = pd.merge(df_customer, df_order, on='CustomerID', how='inner')

print(merged_df)
