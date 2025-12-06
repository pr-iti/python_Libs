import pandas as pd

data = {
  "name": ["Amit Sharma","Priya Verma","Rahul Singh","Neha Kapoor","Vikas Mehra","Sneha Nair","Karan Patel","Divya Reddy","Suresh Rao","Anita D'Souza"
  ],
  "age": [29, 34, 27, 31, 40, 26, 33, 28, 37, 30],
  "salary": [52000, 74000, 48000, 69000, 80000, 45000, 62000, 57000, 76000, 60000],
  "performanceScore": [78, 92, 65, 83, 89, 72, 88, 76, 94, 81]
}

df = pd.DataFrame(data)

print("\n\n",df.head(5).tail(5),"\n\n")
print("displaying dataframe info-------\n\n")
print(df.info(),"\n\n")
print("displaying the descriptive info. of the dataframe----------\n\n")

print(df.describe())
print(f"shape of the dataframe :- ",df.shape)
print(f"no. of column of the dataframe:- ",df.columns)

''''
#output is like this :-------------

           name  age  salary  performanceScore
0  Amit Sharma   29   52000                78
1  Priya Verma   34   74000                92
2  Rahul Singh   27   48000                65
3  Neha Kapoor   31   69000                83
4  Vikas Mehra   40   80000                89


displaying dataframe info-------

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 4 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   name              10 non-null     object
 1   age               10 non-null     int64 
 2   salary            10 non-null     int64 
 3   performanceScore  10 non-null     int64
dtypes: int64(3), object(1)
memory usage: 452.0+ bytes
None


displaying the descriptive info. of the dataframe----------

             age        salary  performanceScore
count  10.000000     10.000000          10.00000
mean   31.500000  62300.000000          81.80000
std     4.503085  12138.551991           9.25923
min    26.000000  45000.000000          65.00000
25%    28.250000  53250.000000          76.50000
50%    30.500000  61000.000000          82.00000
75%    33.750000  72750.000000          88.75000
max    40.000000  80000.000000          94.00000

shape of the dataframe :-  (10, 4)
no. of column of the dataframe:-  Index(['name', 'age', 'salary', 'performanceScore'], dtype='object')  

'''