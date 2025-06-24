import os
import pandas as pd
import tushare as ts
from config import TOKEN, START_DATE, END_DATE
from tushare_helper import get_stock_list, get_stock_data
from filter_logic import is_tianliang

# 初始化 tushare
ts.set_token(TOKEN)
pro = ts.pro_api()

# 创建结果输出目录
os.makedirs("../data/results", exist_ok=True)

# 1. 获取全部A股列表
stocks = get_stock_list(pro)

# 2. 天量筛选
tianliang_list = []
for idx, row in stocks.iterrows():
    ts_code, name = row["ts_code"], row["name"]
    print(f"[{idx+1}/{len(stocks)}] 检测天量：{ts_code} {name}")
    df = get_stock_data(ts_code, START_DATE, END_DATE)
    if df is not None and not df.empty and is_tianliang(df):
        tianliang_list.append({"ts_code": ts_code, "name": name})
df_tianliang = pd.DataFrame(tianliang_list)
df_tianliang.to_excel("../data/results/01_tianliang_filter.xlsx", index=False)
print(f"\n✅ 满足天量条件的股票数：{len(df_tianliang)}，结果已保存至 data/results/01_tianliang_filter.xlsx")
