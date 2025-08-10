import pandas as pd

# read data from csv file into a dataframe
# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# read data from excel file
df = pd.read_excel("SampleSuperstore.xlsx")

# read data from json file 
df = pd.read_json("sample_Data.json")

print(df)