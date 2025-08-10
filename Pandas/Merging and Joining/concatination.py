import pandas as pd

# pd.concat([df1, df2], axis=0, ignore_index=True)

# region1

region1 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'CustomerName': ['Alice', 'Bob', 'Charlie']
})

# region2
region2 = pd.DataFrame({
    'CustomerID': [4, 5],
    'CustomerName': ['David', 'Eve']
})

# Concatenate vertically

df_concat = pd.concat([region1, region2], axis=0, ignore_index=True)
# print(df_concat)

# concatenate horizontally
df_concat_horizontal = pd.concat([region1, region2], axis=1, ignore_index=True)
print(df_concat_horizontal)

