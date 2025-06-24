# 天量选股小工具 (Tianliang Stock Filter)

## 项目简介

本项目为一个自动化A股天量选股脚本，基于 [Tushare](https://tushare.pro/) 接口实现。  
可批量筛选近一年内出现历史最大成交量的股票，并支持自定义多重均线等进阶过滤条件。所有数据本地缓存，易于复用和扩展。

## 功能特点

- 一键批量拉取全A股日线数据（含均线）
- 自动筛选“近一年历史天量”股票
- 支持自定义多重均线过滤（二次筛选）
- 可扩展量能、年涨幅等更多指标
- 结果导出为 Excel 文件，便于后续分析

## 安装依赖

请先确保你的 Python 版本 ≥ 3.8

```bash
pip install -r requirements.txt
```

## 快速开始

1. **注册并获取 Tushare Pro Token**  
   前往 [Tushare Pro官网](https://tushare.pro/register?reg=7) 注册并获取你的专属 token。

2. **配置参数**  
   - 复制 `src/config_template.py` 为 `src/config.py`
   - 打开 `src/config.py`，填写你的 token，并根据需要修改分析区间、均线参数

3. **运行主程序**

   ```bash
   python src/main.py
   ```

4. **查看结果**  
   - 筛选结果将自动保存在 `data/results/01_tianliang_filter.xlsx`

## 目录结构

```
TL_filter/
├── data/                # 本地缓存与结果（已自动 gitignore，不上传）
│   ├── raw/
│   └── results/
├── src/                 # 源码目录
│   ├── main.py
│   ├── config.py / config_template.py
│   ├── tushare_helper.py
│   └── filter_logic.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 进阶用法

- 可在 `src/filter_logic.py` 中自定义或扩展更多筛选规则
- 支持链式多级过滤（天量→均线→其它指标等）
- 欢迎 Fork/PR 二次开发和交流

## 免责声明

- 本项目所有数据与分析结果仅供个人学习与数据处理参考，**不构成任何投资建议**
- 股票投资风险自担，请勿用于任何非法或商业目的

## 致谢

- 感谢 [Tushare](https://tushare.pro/) 为中国金融数据研究提供高质量接口

## License

MIT License
