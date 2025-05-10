import pandas as pd
import numpy as np

bios = pd.read_csv('./bios.csv')

pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.width', None)        # Tự co theo chiều ngang terminal
pd.set_option('display.max_colwidth', 100) # Hiển thị nội dung cột dài

print(bios.head())
bios_new = bios.copy()

# Tách cột name thành các phần tử dựa trên khoảng trắng.
# Lấy phần tử đầu tiên của kết quả tách (tên đầu tiên) và gán vào cột mới first_name
bios_new['first_name'] = bios_new['name'].str.split(" ").str[0]

# Chuyển cột born_date (object) thành kiểu datetime và lưu vào cột mới born_datetime.
bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'])

# Trích xuất năm từ cột born_datetime và gán vào cột mới born_year.
bios_new['born_year'] = bios_new['born_datetime'].dt.year
print(bios_new.info())

