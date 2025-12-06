import pandas as pd

# data = pd.read_excel("SampleSuperstore.xlsx")
data = pd.read_json("sample_Data (1).json")
print("-----------displaying dataframe information-------")
print(data.info())