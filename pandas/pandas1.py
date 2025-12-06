import pandas as pd
import numpy as np

# read csv file to a dataframe
# use gcsfs library to read data from cloud

# df = pd.read_csv("heterogeneous_dataset_extended.csv",encoding="latin1")
df = pd.read_excel("SampleSuperstore.xlsx")
# df = pd.read_json("sample_Data (1).json")

data = pd.DataFrame(df)

# data.to_csv("output1.csv",index = False)
# data.to_json("output1.json")
# data.to_clipboard(excel = True)
# data.to_dict()

data.to_excel("output1.xlsx")

print(df.head(),"\n",df.tail()) #--> returns dy default 5 from head and tail
print("here is file content--------------------------------\n\n")
print(df)
print("\n\n--------here is file content dataframe--------------------------------")
print(data)