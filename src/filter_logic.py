import pandas as pd
from config import MA_LIST, START_DATE, END_DATE

def is_tianliang(df, start_date=START_DATE, end_date=END_DATE):
    """判断近一年内是否出现过历史最大成交量"""
    try:
        if 'vol' not in df.columns or df.empty:
            return False
        max_vol = df['vol'].max()
        df['trade_date'] = pd.to_datetime(df['trade_date'])
        recent = df[(df['trade_date'] >= pd.to_datetime(start_date)) & (df['trade_date'] <= pd.to_datetime(end_date))]
        if recent.empty:
            return False
        max_vol_recent = recent['vol'].max()
        if max_vol_recent == max_vol:
            return True
        return False
    except Exception as e:
        print(f"[天量判定异常] {e}")
        return False

def pass_ma_filter(df, ma_list=MA_LIST):
    """判断最新收盘价是否大于所有指定均线"""
    try:
        if df is None or df.empty:
            return False
        latest = df.sort_values('trade_date', ascending=False).iloc[0]
        for ma in ma_list:
            ma_col = f"ma{ma}"
            if ma_col not in df.columns or pd.isna(latest[ma_col]) or latest['close'] <= latest[ma_col]:
                return False
        return True
    except Exception as e:
        print(f"[均线过滤异常] {e}")
        return False