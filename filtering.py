import pandas as pd

bios = pd.read_csv('./bios.csv')

pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.width', None)        # Tự co theo chiều ngang terminal
pd.set_option('display.max_colwidth', 100) # Hiển thị nội dung cột dài

# lọc theo height_cm và born_country hiển thị 3 cột name, height_cm và
# born_country
print(bios.loc[(bios['height_cm'] > 215) & (bios['born_country'] == "USA"),
['name', 'height_cm', 'born_country']])

# tìm athletes có tên chứa Keith hoặc patrick có phân biệt chữ hoa thường
print(bios.loc[bios['name'].str.contains("Keith|patrick", case=True)])

# dùng regex tìm athletes với tên kết thước bằng son hoặc sen và ko
# có giá trị null cột name
print(bios.loc[bios['name'].str.contains(r'son$|sen$', case=False, na=False)])

# lọc ra những dòng chứa 1 trong các giá trị USA FRA GBR và tên
# bắt đầu bằng Keith có phân biệt chữ hoa thường
print(bios.loc[bios['born_country'].isin(['USA', 'FRA', 'GBR']) &
               bios['name'].str.startswith('Keith')])

# có thể sử dụng query để lọc
print(bios.query('born_country == "USA" and born_city == "Seattle" '))