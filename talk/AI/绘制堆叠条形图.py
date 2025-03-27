import os

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取数据
data_path = os.path.join(os.path.dirname(__file__), '政务数据.csv')
df = pd.read_csv(data_path)

# 计算各区域各类型的诉求量
stack_data = df.groupby(['涉及区域', '投诉类型']).size().unstack()

# 计算各区域平均处理时长
efficiency_data = df.groupby('涉及区域')['处理时长(天)'].mean()

# 创建双Y轴图表
fig, ax1 = plt.subplots(figsize=(14, 8))

# 绘制堆叠柱状图(主Y轴)
stack_data.plot(kind='bar', stacked=True, colormap='tab20', ax=ax1)
ax1.set_title('各区域诉求类型占比与处理时长对比')
ax1.set_xlabel('区域')
ax1.set_ylabel('诉求量', color='b')
ax1.tick_params(axis='y', labelcolor='b')
plt.xticks(rotation=45)

# 创建次Y轴并绘制处理时长折线图
ax2 = ax1.twinx()
ax2.plot(ax1.get_xticks(), efficiency_data, 
        color='r', marker='o', linestyle='--', linewidth=2, markersize=8)
ax2.set_ylabel('平均处理时长(天)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# 添加图例
lines, labels = ax1.get_legend_handles_labels()
ax1.legend(lines, labels, title='投诉类型', bbox_to_anchor=(1.1, 1), loc='upper left')

# 调整布局
plt.tight_layout()

# 保存图片
plt.savefig('堆叠条形图.png', dpi=300, bbox_inches='tight')
print('堆叠柱状图已保存为 堆叠条形图.png')
