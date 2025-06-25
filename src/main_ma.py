# src/main_ma.py
import os
import pandas as pd
from config import START_DATE, END_DATE, RESULT_DIR
from tushare_helper import get_stock_data
from filter_logic import pass_ma_filter

# 读取前一阶段筛选结果
tianliang_path = os.path.join(RESULT_DIR, "01_tianliang_filter.xlsx")
df_tianliang = pd.read_excel(tianliang_path)

ma_results = []

for idx, row in df_tianliang.iterrows():
    ts_code, name = row["ts_code"], row["name"]
    print(f"[{idx+1}/{len(df_tianliang)}] 均线检测：{ts_code} {name}")
    try:
        df = get_stock_data(ts_code, START_DATE, END_DATE)
        if df is None or df.empty:
            continue
        if pass_ma_filter(df):
            ma_results.append({"ts_code": ts_code, "name": name})
    except Exception as e:
        print(f"⚠️ {ts_code} 异常跳过：{e}")
        continue

# 输出结果
output_path = os.path.join(RESULT_DIR, "02_ma_filter.xlsx")
pd.DataFrame(ma_results).to_excel(output_path, index=False)
print(f"\n✅ 完成，结果保存至 {output_path}")
