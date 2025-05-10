import pandas as pd
import numpy as np

coffee = pd.read_csv('./coffee.csv')

# thêm cột price toàn bộ giá trị là 3.99
coffee['price'] = 3.99

# tạo cột mới new_price nếu đk đúng thì gán giá 3.99 sai thì 5.99
coffee['new_price'] = np.where(coffee['Coffee Type']=='Espresso', 3.99, 5.99)

# drop này nó trả về 1 data frame khác đã được xóa
# chứ ko xóa data frame gốc
# xóa dòng có index 0
print(coffee.drop(0))

# nêu có thêm inplace = True thì nó xóa luôn trong data frame gốc
coffee.drop(columns=['price'], inplace=True)
print(coffee)

# tạo 1 bản copy thật sự khi chỉnh sửa coffee_new thì sẽ ko ảnh hưởng
# đến coffee còn nếu mình gán coffee_new = coffee thì khi chỉnh sửa
# coffee_new thì coffee cũng ảnh hưởng
coffee_new = coffee.copy()

# tạo ra cột revenue với mỗi giá trị được lấy từ cột Units Sold
# nhân với cột new_price
coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']
print(coffee)
coffeeRename = coffee.rename(columns={'new_price':'price'})
print(coffeeRename)