import os
import pandas as pd
import tushare as ts
from config import TOKEN, START_DATE, END_DATE, RESULT_DIR
from filter_logic import pass_financial_filter

# 初始化 Tushare
ts.set_token(TOKEN)
pro = ts.pro_api()

# 确保结果目录存在
os.makedirs(RESULT_DIR, exist_ok=True)

# 读取前一阶段结果
ma_path = os.path.join(RESULT_DIR, "02_ma_filter.xlsx")
df_ma = pd.read_excel(ma_path)

# 执行财务筛选
final_list = []
for idx, row in df_ma.iterrows():
    ts_code, name = row["ts_code"], row["name"]
    print(f"[{idx+1}/{len(df_ma)}] 财务过滤：{ts_code} {name}")
    try:
        if pass_financial_filter(pro, ts_code):
            final_list.append({"ts_code": ts_code, "name": name})
    except Exception as e:
        print(f"⚠️ {ts_code} 财务过滤失败：{e}")
        continue

# 保存结果
df_final = pd.DataFrame(final_list)
final_path = os.path.join(RESULT_DIR, "03_final_filter.xlsx")
df_final.to_excel(final_path, index=False)
print(f"\n✅ 财务过滤完成，结果保存至：{final_path}")
