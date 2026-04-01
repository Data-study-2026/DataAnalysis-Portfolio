import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 全局学术配置，符合国奖论文规范
plt.rcParams['font.sans-serif'] = ['SimHei', 'Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 600
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['font.size'] = 10

# 聚类数据：四类群体的核心维度得分（消费金额、情感补偿、身份认同、社群参与度）
# 数据已标准化处理
groups = ['聚类0（浅尝辄止型）', '聚类1（高消费-中情感型）', '聚类2（情感主导型）', '聚类3（深度社群型）']
dimensions = ['消费金额', '情感补偿得分', '身份认同得分', '社群参与度']
# 标准化后得分
scores = np.array([
    [0.12, 0.05, 0.08, 0.21],  # 聚类0
    [0.98, 0.68, 0.72, 0.25],  # 聚类1
    [0.15, 0.95, 0.88, 0.10],  # 聚类2
    [0.18, 0.99, 0.95, 0.98]   # 聚类3
])

# 配色：区分度高，学术风，对应四类群体
colors = ['#1f77b4', '#ff7f0e', '#d62728', '#2ca02c']
# 线条样式：强化群体区分
linestyles = ['-', '--', '-.', ':']
linewidths = [2, 2.5, 2.5, 2.5]

# 绘图：平行坐标图
fig, ax = plt.subplots(figsize=(10, 6))
# 绘制各维度竖线
for i in range(len(dimensions)):
    ax.axvline(x=i, color='gray', linestyle='-', linewidth=0.8, alpha=0.6)
# 绘制四类群体的特征线条
for i in range(len(groups)):
    ax.plot(range(len(dimensions)), scores[i], color=colors[i], label=groups[i],
            linestyle=linestyles[i], linewidth=linewidths[i], marker='o', markersize=4)

# 坐标轴与标注优化
ax.set_xticks(range(len(dimensions)))
ax.set_xticklabels(dimensions, fontsize=11, fontweight=500)
ax.set_ylabel('标准化得分', fontsize=11, fontweight=500)
ax.set_ylim(0, 1.1)
# 图例设置：避免遮挡，布局合理
ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=False, fontsize=9)
# 网格：浅网格，辅助读数
ax.grid(axis='y', linestyle='-', linewidth=0.5, alpha=0.3)
# 标题：规范命名，符合国奖论文图表要求
ax.set_title('图5-1 四类娃衣消费群体核心特征平行坐标图（标准化得分）', fontsize=12, fontweight='bold', pad=20)

# 紧凑布局，保存双格式（EPS矢量图+PNG位图）
plt.tight_layout()
plt.savefig('图5-1 四类娃衣消费群体平行坐标图.eps', format='eps', bbox_inches='tight')
plt.savefig('图5-1 四类娃衣消费群体平行坐标图.png', bbox_inches='tight')
plt.show()
