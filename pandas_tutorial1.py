import pandas as pd

df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9], [10,11,12]],
                  columns=["A", "B", "C"],
                  index=["x", "y", "z", 'zz'])

print(df.head(2))
print(df.tail(2))
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
print(df.nunique())
# df.shape là một tuple, không phải list hay array.
# trả về dòng trước cột sau
print(df.shape)