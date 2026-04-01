import matplotlib.pyplot as plt
import numpy as np

# 全局学术配置，与前文保持一致
plt.rcParams['font.sans-serif'] = ['SimHei', 'Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 600
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['font.size'] = 9
plt.rcParams['grid.alpha'] = 0.3

# 统一配色
colors_amt = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
colors_community = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
colors_impulse = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
colors_decision = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# 数据准备
## 月消费金额
amt_labels = ['100以下', '101-300', '301-500', '501-1000', '1000以上']
amt_values = [11, 144, 158, 56, 31]
## 社群参与频率
com_labels = ['几乎每天', '每周数次', '每月数次', '很少参与', '从不参与']
com_values = [80, 160, 100, 40, 20]
## 情感冲动购买倾向
imp_labels = ['非常不同意', '不同意', '一般', '同意', '非常同意']
imp_values = [20, 40, 100, 120, 120]
## 购买决策因素（雷达图）
dec_labels = ['独特设计', '面料质感', '限量标签', '价格合理性', '设计师知名度']
dec_values = [3.97, 3.87, 3.70, 3.25, 3.15]
# 雷达图角度设置
angles = np.linspace(0, 2*np.pi, len(dec_labels), endpoint=False).tolist()
dec_values += dec_values[:1]
angles += angles[:1]
dec_labels += dec_labels[:1]

# 构建2*2子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

# 1. 月消费金额柱状图
ax1 = axes[0]
bars1 = ax1.bar(amt_labels, amt_values, color=colors_amt, edgecolor='black', linewidth=0.8)
ax1.set_title('（a）月消费金额分布', fontsize=10, fontweight='bold', pad=10)
ax1.set_ylabel('人数', fontsize=9)
for bar, val in zip(bars1, amt_values):
    ax1.text(bar.get_x()+bar.get_width()/2, bar.get_height()+2, val, ha='center', va='bottom', fontsize=8)
ax1.grid(axis='y')

# 2. 社群参与频率柱状图
ax2 = axes[1]
bars2 = ax2.bar(com_labels, com_values, color=colors_community, edgecolor='black', linewidth=0.8)
ax2.set_title('（b）社群参与频率分布', fontsize=10, fontweight='bold', pad=10)
ax2.set_ylabel('人数', fontsize=9)
for bar, val in zip(bars2, com_values):
    ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+3, val, ha='center', va='bottom', fontsize=8)
ax2.tick_params(axis='x', rotation=10)
ax2.grid(axis='y')

# 3. 情感冲动购买倾向柱状图
ax3 = axes[2]
bars3 = ax3.bar(imp_labels, imp_values, color=colors_impulse, edgecolor='black', linewidth=0.8)
ax3.set_title('（c）情感冲动购买倾向分布', fontsize=10, fontweight='bold', pad=10)
ax3.set_ylabel('人数', fontsize=9)
for bar, val in zip(bars3, imp_values):
    ax3.text(bar.get_x()+bar.get_width()/2, bar.get_height()+3, val, ha='center', va='bottom', fontsize=8)
ax3.tick_params(axis='x', rotation=10)
ax3.grid(axis='y')

# 4. 购买决策因素雷达图
ax4 = axes[3]
ax4.plot(angles, dec_values, color='#1f77b4', linewidth=2, marker='o', markersize=4)
ax4.fill(angles, dec_values, color='#1f77b4', alpha=0.2)
ax4.set_xticks(angles[:-1])
ax4.set_xticklabels(dec_labels[:-1], fontsize=8)
ax4.set_ylim(0, 5)
ax4.set_title('（d）购买决策因素得分', fontsize=10, fontweight='bold', pad=10)
ax4.grid(True)
# 添加数值标签
for i, val in enumerate(dec_values[:-1]):
    ax4.text(angles[i], val+0.1, f'{val:.2f}', ha='center', va='bottom', fontsize=8, fontweight='bold')

# 总标题
fig.suptitle('图4-2 娃衣消费样本消费行为特征分布', fontsize=12, fontweight='bold', y=0.98)

# 紧凑布局，保存双格式
plt.tight_layout()
plt.savefig('图4-2 消费行为特征分布.eps', format='eps', bbox_inches='tight')
plt.savefig('图4-2 消费行为特征分布.png', bbox_inches='tight')
plt.show()
