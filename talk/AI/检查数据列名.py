import pandas as pd
import os

# 读取数据
data_path = os.path.join(os.path.dirname(__file__), '政务数据.csv')
df = pd.read_csv(data_path)

# 打印列名和数据样例
print("数据列名:", df.columns.tolist())
print("\n数据样例:")
print(df.head())
