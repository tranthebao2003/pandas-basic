import pandas as pd

coffee = pd.read_csv('./coffee.csv')
print(coffee.head())

# lọc
# coffee.loc[#Row, #Columns]
print(coffee.loc[0])

# lọc 3 dòng 0,1,5
print(coffee.loc[[0,1,5]])

# lọc từ dòng 0 đến hết
print(coffee.loc[0:])

# lọc từ dòng 6 đến dòng 12
print(coffee.loc[6:12])

# lọc từ dòng 6 đến dòng 12 cột Day, Units Sold
print(coffee.loc[6:12, ["Day", "Units Sold"]])

# iloc lọc từ dòng 6 đến dòng 12 cột Day,
# Units Sold nhưng dùng index của cột thay vì tên
print(coffee.iloc[6:12, [0,2]])

# chính sửa value: chọn dòng 1 và cột Units Sold
coffee.loc[1, "Units Sold"] = 10
print(coffee.head())

# chính sửa value: chọn dòng 1 đến 3 và cột Units Sold
coffee.loc[1:3, "Units Sold"] = 10
print(coffee.head())

# gán cột day cho cột index (cột tự sinh ra)
coffee.index = coffee["Day"]
print(coffee.head())


