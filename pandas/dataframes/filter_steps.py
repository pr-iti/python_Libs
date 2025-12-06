'''
1. select specific column -> square brackets
2. filter rows -> boolean codn.
3. combine multiple codn.

selecting cols. returns
1. a series
2. dataframes(multiplpe rows and column)

column = df["column name]
subset = df['col1',col2',......]


filtering uses and returns
1. bollean indexing

#based on single codn.
filtred_rows = df[df["col_name] > value]

#based on multiple codn.
filtred_rows = df[(df["col_name] > value1]) &(df["col_name] < value2])]

'''

import pandas as pd

data = {
  "name": ["Amit Sharma","Priya Verma","Rahul Singh","Neha Kapoor","Vikas Mehra","Sneha Nair","Karan Patel","Divya Reddy","Suresh Rao","Anita D'Souza"
  ],
  "age": [29, 34, 27, 31, 40, 26, 33, 28, 37, 30],
  "salary": [52000, 74000, 48000, 69000, 80000, 45000, 62000, 57000, 76000, 60000],
  "performanceScore": [78, 92, 65, 83, 89, 72, 88, 76, 94, 81]
}

df = pd.DataFrame(data)

# print("#----------------------------------------------")
# print("#       column filter")

# print("#--------------------------------------------------")

# print(df[df["salary"] > 52000]) # select /filter single col
# print(df[(df["salary"] > 52000) & (df["salary"] < 80000)])  # select /filter multiple col

# subset = df[["name","salary"]] #select multiple col
# print(subset)



# print("#----------------------------------------------")
# print("#       rows filter")
# print("#--------------------------------------------------")

# print("data of the employees salary more than 48000")
# print(df[df["salary"] > 48000])

# filtered = df[(df['salary'] > 55000) & (df['age'] > 30)]

# print("employees with age and salary filter ")
# print(filtered)

filteredwith_or = df[(df['performanceScore'] >= 85) | (df['age'] > 30)]
print("-------------- employees filtered with age and performance  ------------")
print(filteredwith_or)