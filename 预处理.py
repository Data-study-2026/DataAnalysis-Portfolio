import pandas as pd
import numpy as np
import re
from datetime import datetime

# 读取数据
df = pd.read_excel("附件.xlsx", sheet_name="男胎检测数据")

# 1. 处理缺失值
# 对于数值列，使用中位数填充
numeric_cols = ['年龄', '身高', '体重', '原始读段数', '在参考基因组上比对的比例', 
                '重复读段的比例', '唯一比对的读段数', 'GC含量', '13号染色体的Z值', 
                '18号染色体的Z值', '21号染色体的Z值', 'X染色体的Z值', 'Y染色体的Z值', 
                'Y染色体浓度', 'X染色体浓度', '13号染色体的GC含量', '18号染色体的GC含量', 
                '21号染色体的GC含量', '被过滤掉读段数的比例']

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)

# 对于分类列，使用众数填充
categorical_cols = ['IVF妊娠', '染色体的非整倍体', '怀孕次数', '生产次数', '胎儿是否健康']
for col in categorical_cols:
    if col in df.columns:
        if df[col].dtype == 'object':
            mode_val = df[col].mode()[0] if not df[col].mode().empty else '未知'
            df[col].fillna(mode_val, inplace=True)
        else:
            mode_val = df[col].mode()[0] if not df[col].mode().empty else 0
            df[col].fillna(mode_val, inplace=True)

# 2. 统一日期格式
date_cols = ['末次月经', '检测日期']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# 3. 提取数值型孕周
def extract_weeks(s):
    if pd.isna(s):
        return np.nan
    if isinstance(s, str):
        if '+' in s:
            parts = re.findall(r'(\d+)\s*[wW]\s*\+\s*(\d+)', s)
            if parts:
                weeks, days = map(int, parts[0])
                return weeks + days/7.0
        else:
            weeks = re.findall(r'(\d+)\s*[wW]', s)
            if weeks:
                return float(weeks[0])
    return np.nan

df['检测孕周数值'] = df['检测孕周'].apply(extract_weeks)
df['检测孕周数值'].fillna(df['检测孕周数值'].median(), inplace=True)

# 4. 处理异常值 - 将负的Y染色体浓度设为0
if 'Y染色体浓度' in df.columns:
    df.loc[df['Y染色体浓度'] < 0, 'Y染色体浓度'] = 0

# 5. 编码分类变量 - 不使用sklearn的LabelEncoder
# 创建映射字典
ivf_mapping = {'自然受孕': 0, 'IVF妊娠': 1, '未知': 2}
health_mapping = {'是': 1, '否': 0, '未知': 2}

if 'IVF妊娠' in df.columns:
    df['IVF妊娠'] = df['IVF妊娠'].map(ivf_mapping).fillna(2)  # 默认值为2(未知)

if '胎儿是否健康' in df.columns:
    df['胎儿是否健康'] = df['胎儿是否健康'].map(health_mapping).fillna(2)  # 默认值为2(未知)

# 6. 处理重复记录 - 保留第一次出现的记录
df.drop_duplicates(subset=['孕妇代码', '检测日期'], keep='first', inplace=True)

# 7. 计算BMI
df['计算BMI'] = df['体重'] / ((df['身高'] / 100) ** 2)

# 8. 删除不必要的列
columns_to_drop = ['检测孕周', '孕妇BMI']  # 保留原始BMI列供比较
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

# 9. 重置索引
df.reset_index(drop=True, inplace=True)

# 10. 保存预处理后的数据
df.to_csv("预处理后_男胎检测数据.csv", index=False, encoding='utf-8-sig')

print("数据预处理完成！已保存为 '预处理后_男胎检测数据.csv'")
print(f"处理后数据形状: {df.shape}")
print("\n前5行数据:")
print(df.head().to_string())
