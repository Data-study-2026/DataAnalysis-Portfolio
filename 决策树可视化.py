import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# ----------------------1. 数据读取与预处理----------------------
file_path = "D:/Users/Lenovo/Desktop/2025-2026市调/市调源数据-序号版.xlsx"
data = pd.read_excel(file_path, sheet_name="Sheet1")

# 用列索引定位（避免列名问题）
data_selected = data.iloc[:, [23, 22, 10, 9, 18]].copy()
data_selected.columns = ["收入", "城市级别", "独特设计认同", "视频平台使用", "情绪调节效果"]
data_clean = data_selected.dropna()

# 编码与二值化
le = LabelEncoder()
data_clean["收入"] = le.fit_transform(data_clean["收入"])
data_clean["城市级别"] = le.fit_transform(data_clean["城市级别"])
data_clean["视频平台使用"] = data_clean["视频平台使用"].astype(int)
data_clean["情绪调节效果"] = (data_clean["情绪调节效果"] >= 4).astype(int)

X = data_clean[["收入", "城市级别", "独特设计认同", "视频平台使用"]]
y = data_clean["情绪调节效果"]

# ----------------------2. 模型训练----------------------
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,  # 深度控制为3，保证简洁无杂乱小方块
    min_samples_split=20,
    min_samples_leaf=10,
    class_weight="balanced",
    random_state=42
)
model.fit(X, y)

# ----------------------3. 修正版矢量图可视化（核心）----------------------
# 设置全局字体（解决中文乱码，适配论文）
plt.rcParams["font.family"] = "SimHei"  # 黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示

# 创建高清画布（16:9比例适配论文版面）
fig, ax = plt.subplots(figsize=(16, 9), dpi=300)

# 绘制简洁版决策树（移除错误的cmap参数，保留核心美化设置）
plot_tree(
    model,
    ax=ax,
    feature_names=["月可支配收入", "城市级别", "独特设计认同", "视频平台使用"],
    class_names=["低购买意愿", "高购买意愿"],
    filled=True,          # 颜色填充（用默认学术配色，柔和不刺眼）
    rounded=True,         # 圆角矩形，彻底去掉"小方块"生硬感
    fontsize=11,          # 字体大小适配论文阅读
    max_depth=3,          # 严格限制深度，避免分支过多
    impurity=False,       # 隐藏基尼系数（非核心信息）
    node_ids=False,       # 隐藏节点ID
    proportion=False,     # 隐藏样本比例
    precision=1           # 数值简化，仅保留1位小数
)

# 标题优化（学术风格）
ax.set_title("娃衣购买意愿决策树", fontsize=18, pad=25, fontweight="bold")
plt.tight_layout()  # 自动调整布局，避免文字重叠

# ----------------------4. 保存矢量图（论文专用）----------------------
# 保存SVG矢量图（无像素模糊，可无限放大）
plt.savefig("娃衣决策树_论文版.svg", format="svg", bbox_inches="tight")
# 备用高清PNG（300dpi，兼容所有编辑器）
plt.savefig("娃衣决策树_论文版.png", dpi=300, bbox_inches="tight")

plt.show()
