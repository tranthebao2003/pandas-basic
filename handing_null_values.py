import pandas as pd
import numpy as np

bios = pd.read_csv('./bios.csv')

pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.width', None)        # Tự co theo chiều ngang terminal
pd.set_option('display.max_colwidth', 100) # Hiển thị nội dung cột dài
