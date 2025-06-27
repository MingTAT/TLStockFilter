# TLStockFilter

一个基于成交量“天量突破”、多周期均线验证与基本面筛选的 A 股量化选股工具。

## 📌 项目简介

TLStockFilter 是一个以数据为核心的选股系统，旨在辅助投资者筛选出具有潜力的A股标的。其核心逻辑分为三步：

1. 筛出近一年出现**历史最大成交量**的股票；
2. 判断其是否**当前价格站上所有关键均线**；
3. 最后依据**财务稳健性（净利润为正、PB 合理、涨幅不过高）**进一步筛选。

所有逻辑基于 [Tushare Pro](https://tushare.pro) 数据实现，结果导出为 Excel 文件供分析使用。

---

## ✅ 筛选流程概览

### Step 1：历史天量筛选  
- 时间区间：近一年（默认 `2024-06-24 ~ 2025-06-24`）  
- 判定标准：该时间段内的最大成交量 = 股票历史最大成交量

### Step 2：多周期均线验证  
- 当前收盘价 > 所有指定均线  
- 默认均线：`60, 120, 250, 610, 850, 985`  
- 需使用 `adj='qfq'` 前复权数据

### Step 3：基本面过滤  
- `净利润 > 0`
- `PB ∈ (0, 3)`
- `年涨幅 < 50%`

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/MingTAT/TLStockFilter.git
cd TLStockFilter
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 Tushare Token

复制模板文件：

```bash
cp src/config_template.py src/config.py
```

然后在 `src/config.py` 中填写你的 Tushare Token：

```python
TOKEN = "your_tushare_token"
```

### 4. 按顺序执行筛选流程

```bash
# 步骤一：筛选历史天量
python src/main.py

# 步骤二：均线筛选
python src/main_ma.py

# 步骤三：基本面筛选
python src/main_final.py
```

结果输出路径为：

```
data/results/01_tianliang_filter.xlsx
data/results/02_ma_filter.xlsx
data/results/03_final_filter.xlsx
```

---

## 📁 项目结构

```
TLStockFilter/
│
├── data/
│   ├── raw/               # 原始数据缓存
│   └── results/           # 筛选结果
│
├── src/
│   ├── config.py          # 配置（含 Token 与日期）
│   ├── config_template.py # 配置模板
│   ├── main.py            # 第一步：历史天量筛选
│   ├── main_ma.py         # 第二步：均线条件筛选
│   ├── main_final.py      # 第三步：财务条件筛选
│   ├── tushare_helper.py  # 数据拉取工具
│   └── filter_logic.py    # 筛选逻辑定义
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📌 示例输出（示意）

| 股票代码 | 股票名称 | 筛选阶段     |
|----------|----------|--------------|
| 000001.SZ | 平安银行 | ✅ 财务通过 |
| 600519.SH | 贵州茅台 | ✅ 财务通过 |
| 300750.SZ | 宁德时代 | ✅ 财务通过 |

---

## ⚠️ 免责声明

本项目仅供学习与研究使用，所含内容不构成投资建议。所有投资决策请依据个人判断，自行承担风险。

---

## 📮 联系与支持

欢迎提交 [Issues](https://github.com/MingTAT/TLStockFilter/issues) 或 PR 以改进项目。如有合作意向，可通过 GitHub 私信联系。

---

Made with ❤️ by [MingTAT](https://github.com/MingTAT)
