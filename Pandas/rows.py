# head() tail()
# head(n) and tail(n) where n = number of rows to display 
# n's default value is 5

import pandas as pd

# Read CSV with proper encoding
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

print("Display 10 Rows of First:")
print(df.head(10))

print("Display 10 Rows of Last:")
print(df.tail(10))
