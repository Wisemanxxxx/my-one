# FinMind-Orbit

基于长链推理的全自动行业研报生成 Agent 系统 | 日均Token消耗 ~1200万

## 项目简介

FinMind-Orbit 是一个面向金融投研领域的多Agent协作系统，采用Meta-Planning加多Agent执行架构，将传统3天的人工撰写流程压缩至2小时内。

## 系统架构

用户请求 -> 规划Agent(任务拆解) -> 爬取Agent -> 解析Agent -> 验证Agent -> 撰写Agent -> 输出报告

## 快速开始

### 环境要求
- Python 3.10+
- MiMo API Key

### 安装步骤

1. 克隆仓库
2. pip install -r requirements.txt
3. 配置.env文件中的MIMO_API_KEY
4. python src/main.py

## 量化成果

- 日均Token消耗: ~1200万
- 单份研报产出时间: < 2小时
- 数据准确率: 98%以上
- 已处理财报: 87份
- 已生成研报: 23篇

## License

MIT License