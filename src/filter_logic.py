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
    

def pass_financial_filter(pro, ts_code):
    try:
        # 获取最近一个交易日
        latest_trade_date = pro.trade_cal(
            exchange='', start_date='20250601', end_date='20250624', is_open='1'
        ).sort_values('cal_date', ascending=False).iloc[0]['cal_date']

        # 获取净利润
        income = pro.fina_indicator(
            ts_code=ts_code, period=latest_trade_date, fields="ts_code,netprofit"
        )
        if income.empty or income.iloc[0]['netprofit'] <= 0:
            return False

        # 获取PB
        basic = pro.daily_basic(
            ts_code=ts_code, trade_date=latest_trade_date, fields="pb,close"
        )
        if basic.empty:
            return False

        pb = basic.iloc[0]['pb']
        if not (0 < pb < 3):
            return False

        # 获取近一年涨幅
        df = pro.daily(
            ts_code=ts_code,
            start_date='20240624', end_date='20250624',
            fields='ts_code,trade_date,close'
        )
        df = df.sort_values("trade_date", ascending=False)
        if df.empty or len(df) < 2:
            return False

        pct_chg = (df.iloc[0]['close'] - df.iloc[-1]['close']) / df.iloc[-1]['close'] * 100
        if pct_chg > 50:
            return False

        return True

    except Exception as e:
        print(f"[财务过滤异常] {ts_code}: {e}")
        return False
