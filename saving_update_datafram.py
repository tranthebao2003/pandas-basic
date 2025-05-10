import pandas as pd
import numpy as np

bios = pd.read_csv('./bios.csv')

pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.width', None)        # Tự co theo chiều ngang terminal
pd.set_option('display.max_colwidth', 100) # Hiển thị nội dung cột dài

print(bios.head())
bios_new = bios.copy()
# lưu file csv mới
# bios_new.to_csv('./bios_new.cvs', index=False)


# Mục đích: Phân loại chiều cao thành 3 nhóm:
# Short: Dưới 165 cm.
# Average: Từ 165 cm đến dưới 185 cm.
# Tall: Từ 185 cm trở lên.
# Cơ chế:
# Sử dụng apply với lambda function để kiểm tra từng giá trị trong cột height_cm.
# Điều kiện lồng nhau:
bios['height_category'] = bios['height_cm'].apply(
    lambda x: 'Short' if x < 165 else ('Average' if x < 185 else 'Tall'))
print(bios)

# Mục đích: Phân loại vận động viên dựa trên cả chiều cao và cân nặng
def categorize_athlete(row):
    if row['height_cm'] < 175 and row ['weight_kg'] < 70:
        return 'LightWeight'
    elif row['height_cm'] < 185 and row['weight_kg'] <= 80:
        return 'Middleweight'
    else:
        return 'Heavyweight'

# Hàm categorize_athlete nhận từng hàng (row) của DataFrame và trả về phân loại dựa trên điều kiện.
# Sử dụng apply với axis=1 để áp dụng hàm này cho từng hàng.
bios['Category'] = bios.apply(categorize_athlete, axis=1)
print(bios)