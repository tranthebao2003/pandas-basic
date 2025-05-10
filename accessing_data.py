import pandas as pd

coffee = pd.read_csv('./coffee.csv')

# mặc định là ascending
# nó sắp xếp theo Units sold trước sau đó nào giống nhau
# thì nó lại sắp xếp theo Coffee Type
print(coffee.sort_values(["Units Sold", "Coffee Type"], ascending=False))

# lặp qua từng dòng
for index, row in coffee.iterrows():
    print(index)
    print(row)
    print("\n\n\n\n\n")
