import pandas as pd
import numpy as np

coffee = pd.read_csv('./coffee.csv')

pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.width', None)        # Tự co theo chiều ngang terminal
pd.set_option('display.max_colwidth', 100) # Hiển thị nội dung cột dài

coffee.loc[[0,1], 'Units Sold'] = np.nan

# isna(): Tạo DataFrame boolean (True/False) đánh dấu vị trí các giá trị NaN.
# sum(): Tính tổng số lượng True (NaN) theo từng cột.
print(coffee.isna().sum())

# coffee['Units Sold'].isna(): Tạo mask boolean cho các hàng có giá trị NaN ở cột 'Units Sold'.
# Lọc và in ra các hàng thỏa mãn điều kiện này.
print(coffee[coffee['Units Sold'].isna()])

# coffee['Units Sold'].mean(): Tính giá trị trung bình của cột 'Units Sold'.
# fillna(): Thay thế tất cả giá trị NaN trong toàn bộ DataFrame bằng giá trị trung bình này.
print(coffee.fillna(coffee['Units Sold'].mean()))

# coffee['Units Sold'].interpolate(): Nội suy giá trị cho cột 'Units Sold', nhưng kết quả trả về một Series đã được điền.
print(coffee.fillna(coffee['Units Sold'].interpolate()))

#  Xóa mọi hàng có ít nhất một giá trị NaN.
print(coffee.dropna())
print(coffee)