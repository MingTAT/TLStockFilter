import os
import pandas as pd
import tushare as ts
from config import TOKEN

def get_stock_list(pro):
    """获取A股全部上市股票代码及名称"""
    return pro.stock_basic(exchange='', list_status='L', fields='ts_code,name')

def get_stock_data(ts_code, start_date, end_date):
    """获取单只股票上市以来全部日线行情，包含指定均线，自动缓存为csv"""
    cache_dir = "data/raw"
    os.makedirs(cache_dir, exist_ok=True)
    cache_path = os.path.join(cache_dir, f"{ts_code.replace('.', '_')}.csv")
    if os.path.exists(cache_path):
        df = pd.read_csv(cache_path)
        df['trade_date'] = pd.to_datetime(df['trade_date'])
        df = df.sort_values('trade_date', ascending=False).reset_index(drop=True)
        return df
    # 如果没有缓存，拉取全历史数据
    df = ts.pro_bar(
        ts_code=ts_code, 
        adj='qfq',
        start_date="20000101",
        end_date=end_date.replace('-', ''),
        ma=[60, 120, 250, 610, 850, 985]
    )
    if df is None or df.empty:
        return None
    df = df.sort_values('trade_date', ascending=False).reset_index(drop=True)
    df['trade_date'] = pd.to_datetime(df['trade_date'])
    df.to_csv(cache_path, index=False)
    return df
