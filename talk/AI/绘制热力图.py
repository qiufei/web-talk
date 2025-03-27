import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取数据
import os

data_path = os.path.join(os.path.dirname(__file__), '政务数据.csv')
df = pd.read_csv(data_path)

# 1. 诉求量热力图数据
heatmap_data = pd.crosstab(df['涉及区域'], df['投诉类型'])

# 2. 处理效率和满意度数据
efficiency_data = df.groupby(['涉及区域', '投诉类型'])['处理时长(天)'].mean().unstack()
satisfaction_data = df.groupby(['涉及区域', '投诉类型'])['满意度(1-5)'].mean().unstack()

# 创建图形
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

# 绘制诉求量热力图
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd', 
           linewidths=.5, ax=ax1)
ax1.set_title('各区域诉求类型分布热力图(颜色深浅表示诉求量)')
ax1.set_xlabel('投诉类型')
ax1.set_ylabel('涉及区域')

# 绘制处理效率/满意度热力图
combined_data = efficiency_data.applymap(lambda x: f"{x:.1f}天") + "\n" + \
               satisfaction_data.applymap(lambda x: f"{x:.1f}分")
sns.heatmap(satisfaction_data, annot=combined_data, fmt='s',
           cmap='RdYlGn', center=3, linewidths=.5, ax=ax2)
ax2.set_title('处理时长(天)和满意度(1-5分)热力图\n(红色表示处理慢/满意度低,绿色相反)')
ax2.set_xlabel('投诉类型')
ax2.set_ylabel('涉及区域')

plt.tight_layout()
plt.savefig('热力图.png')
print('热力图已保存为 热力图.png')
