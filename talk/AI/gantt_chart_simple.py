import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.font_manager as fm

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 读取数据
data = pd.read_csv("qmd/项目进度数据.csv")
data['开始日期'] = pd.to_datetime(data['开始日期'])
data['结束日期'] = pd.to_datetime(data['结束日期'])
data['关键路径'] = data['阶段名称'] == '系统迁移'

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))
colors = {'已完成': '#4CAF50', '进行中': '#2196F3', '未开始': '#9E9E9E'}

for _, row in data.iterrows():
    ax.barh(row['阶段名称'], 
           (row['结束日期'] - row['开始日期']).days,
           left=row['开始日期'],
           color=colors[row['状态']],
           edgecolor='red' if row['关键路径'] else 'none',
           linewidth=2 if row['关键路径'] else 0.5)
    
    # 添加进度文本
    ax.text(row['结束日期'], 
            row['阶段名称'], 
            f"{row['进度百分比']}%",
            va='center', ha='left')

ax.set_xlabel('时间')
ax.set_title('项目进度甘特图')
ax.xaxis_date()
plt.tight_layout()

# 保存图片
plt.savefig("qmd/gantt_chart.png", dpi=300, bbox_inches='tight')
plt.close()

print("甘特图已保存为 qmd/gantt_chart.png，请手动插入PPT")
