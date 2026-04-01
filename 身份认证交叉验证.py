import matplotlib.pyplot as plt
import numpy as np

# 全局学术配置，保持全文统一性
plt.rcParams['font.sans-serif'] = ['SimHei', 'Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 600
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['font.size'] = 10

# 核心量化数据
identity_score = 3.50  # 群体归属认同得分
interaction_sizes = [40, 60]  # 高频/低频互动占比
interaction_labels = ['高频互动\n（每日/每周）', '低频互动\n（偶尔/从不）']
# 学术配色：暖色调突出核心，灰色衬托次要
colors_main = ['#F39C12', '#BDC3C7']

# 绘图（1行2列，适配论文通栏，宽度比例优化）
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5), gridspec_kw={'width_ratios': [1, 1.2]})

# 左图：群体归属认同均值柱形图
bar1 = ax1.bar(
    ['群体归属认同'], [identity_score],
    width=0.3,
    color=colors_main[0],
    edgecolor='black',
    linewidth=0.8,
    zorder=2
)
# 标注精准分值
ax1.text(
    0, identity_score + 0.15,
    f'{identity_score:.2f}',
    ha='center',
    va='bottom',
    fontweight='bold',
    fontsize=11
)
ax1.set_ylim(0, 5)
ax1.set_ylabel('得分（5分制）', fontsize=11, fontweight='500')
ax1.set_title('（a）群体归属认同得分', fontsize=11, fontweight='bold')
ax1.grid(axis='y', linestyle='-', linewidth=0.5, zorder=1)

# 右图：社群互动频率环形图（学术优选，避免普通饼图的臃肿感）
wedges, texts, autotexts = ax2.pie(
    interaction_sizes,
    labels=interaction_labels,
    autopct='%1.1f%%',
    colors=colors_main,
    startangle=90,
    wedgeprops=dict(
        width=0.35,  # 环形宽度优化
        edgecolor='black',
        linewidth=0.8,
        zorder=2
    ),
    textprops={'fontsize': 9.5},
    pctdistance=0.75,
    labeldistance=1.15
)
# 优化百分比字体，增强可读性
for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

ax2.set_title('（b）社群互动频率分布', fontsize=11, fontweight='bold')

# 总标题：规范命名，明确跨维度属性
fig.suptitle('图6-3 身份认同维度：群体归属与社群互动行为交叉验证', fontsize=12, fontweight='bold', y=1.02)

plt.tight_layout()
# 保存双格式，适配不同使用场景
plt.savefig('图6-3 社群归属与身份认同验证图.eps', format='eps', bbox_inches='tight')
plt.savefig('图6-3 社群归属与身份认同验证图.png', bbox_inches='tight')
plt.show()
