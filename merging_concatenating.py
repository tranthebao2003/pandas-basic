import pandas as pd
import numpy as np

nocs = pd.read_csv('./noc_regions.csv')
bios = pd.read_csv('./bios.csv')
pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.width', None)        # Tự co theo chiều ngang terminal
pd.set_option('display.max_colwidth', 100) # Hiển thị nội dung cột dài

print(nocs)
print(bios)

# Mục đích: Kết hợp dữ liệu từ hai DataFrame bios và nocs dựa trên mã quốc gia.
# Chi tiết:
# left_on='born_country': Cột born_country trong DataFrame bios (mã quốc gia 3 ký tự, ví dụ: "USA").
# right_on='NOC': Cột NOC trong DataFrame nocs (thường chứa mã quốc gia Olympic, ví dụ: "USA").
# how='left': Giữ lại tất cả hàng từ bios, chỉ thêm dữ liệu từ nocs nếu khớp.
# suffixes=("_bios", "_nocdf"): Thêm hậu tố để phân biệt cột trùng tên từ hai DataFrame
# (ví dụ: region_bios, region_nocdf nếu cả hai đều có cột region).
bios_new_merge = pd.merge(bios, nocs, left_on='born_country', right_on='NOC', how='left', suffixes=("bios", "nocdf"))

# Mục đích: Đổi tên cột region (lấy từ nocs) thành born_country_full để thể hiện
# tên đầy đủ của quốc gia sinh.
bios_new_merge.rename(columns={'region':'born_country_full'}, inplace=True )
print(bios_new_merge)

# Mục đích: Tạo hai DataFrame con chỉ chứa dữ liệu của vận động viên từ Mỹ (USA) và Anh (GBR).
# Chi tiết:
# .copy(): Tạo bản sao độc lập để tránh thay đổi dữ liệu gốc trong bios
usa = bios[bios['born_country'] == 'USA'].copy()
gbr = bios[bios['born_country'] == 'GBR'].copy()

# Mục đích: Kết hợp dữ liệu từ hai quốc gia vào một DataFrame mới new_df.
# Kết quả: new_df chứa tất cả hàng từ usa và gbr.
new_df = pd.concat([usa, gbr])
print(new_df)