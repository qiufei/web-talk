import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import os

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取数据
data_path = os.path.join(os.path.dirname(__file__), '政务数据.csv')
df = pd.read_csv(data_path)

# 计算各区域各投诉类型的诉求量
df['诉求量'] = df.groupby(['涉及区域', '投诉类型'])['投诉类型'].transform('count')

# 绘制气泡图
plt.figure(figsize=(14, 8))
scatter = sns.scatterplot(
    data=df,
    x='处理时长(天)',
    y='满意度(1-5)',
    hue='投诉类型',  # 用颜色区分投诉类型
    size='诉求量',   # 用大小表示诉求量
    sizes=(30, 500), # 设置气泡大小范围
    alpha=0.7,
    palette='tab20'  # 使用丰富的颜色
)

# 添加趋势线
sns.regplot(
    data=df,
    x='处理时长(天)',
    y='满意度(1-5)',
    scatter=False,
    color='gray',
    line_kws={'linestyle':'--'}
)

# 标记异常点
anomaly = df[(df['处理时长(天)'] > 5) & (df['满意度(1-5)'] < 2)]
for _, row in anomaly.iterrows():
    plt.text(
        row['处理时长(天)']+0.1,
        row['满意度(1-5)'],
        row['投诉类型'],
        fontsize=10
    )

plt.title('处理时长与满意度关系气泡图\n(气泡大小表示诉求量)')
plt.xlabel('处理时长(天)')
plt.ylabel('满意度(1-5分)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# 保存图片
plt.savefig('散点图.png', dpi=300, bbox_inches='tight')
print('散点图已保存为 散点图.png')
