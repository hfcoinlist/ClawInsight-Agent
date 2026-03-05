# 🦅 ClawInsight: The OpenClaw-Powered Smart Guardian for Binance

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Binance API](https://img.shields.io/badge/Binance-API-F3BA2F?logo=binance&logoColor=white)](https://binance-docs.github.io/apidocs/spot/en/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Build the future of Crypto AI.** > ClawInsight 是一款专为 **Binance OpenClaw Campaign** 打造的 Web3 智能投研与资产管理助手。它通过融合大语言模型（LLM）与链上情绪数据，重新定义了散户的交易体验。

---

## 📑 目录 (Table of Contents)
1. [项目背景 (The Problem)](#1-项目背景-the-problem)
2. [核心架构 (Architecture)](#2-核心架构-architecture)
3. [关键特性 (Key Features)](#3-关键特性-key-features)
4. [安装与部署 (Installation & Setup)](#4-安装与部署-installation--setup)
5. [应用场景示例 (Use Cases)](#5-应用场景示例-use-cases)
6. [发展路线图 (Roadmap)](#6-发展路线图-roadmap)

---

## 1. 💡 项目背景 (The Problem)
在当今的加密市场，普通投资者面临三大核心痛点：
- **信息过载 (Info-Overload)**：币安广场 (Binance Square) 和 X 上充斥着海量噪音和情绪化的“喊单”，普通人难以分辨真伪。
- **机械的定投 (Rigid DCA)**：传统的定投策略无视市场情绪。
- **高位套牢的焦虑**：许多投资者在牛市高点建仓，缺乏科学的补仓降本策略。

**ClawInsight 的使命**：将复杂的市场情绪提炼为清晰的执行信号。让 AI 成为用户的“交易理智”，在极度贪婪时提醒风险，在极度恐慌时规划加仓。

---

## 2. 🏗️ 核心架构 (Architecture)

ClawInsight 采用三层模块化设计，确保高扩展性与极佳的安全性：

* **Data Layer (数据感知层)**:
  * Binance Rest API: 获取现货、合约的实时 K 线与深度数据。
  * OpenClaw SDK: 实时抓取并清洗币安生态及全网的社交媒体文本。
* **Brain Layer (AI 决策大脑)**:
  * NLP 情感分析引擎：过滤机器水军，提取真实的“市场恐慌/贪婪度”。
  * 动态算法模型：将用户的持仓成本与 AI 情绪指数加权计算。
* **Execution Layer (执行与分发层)**:
  * 终端 CLI 交互反馈。
  * 自动化研报生成与推送系统。

---

## 3. ✨ 关键特性 (Key Features)

### 🧠 1. OpenClaw 情绪指数引擎
不再依赖滞后的技术指标。系统通过 AI 实时阅读成千上万条社区帖子，输出 0.0 (极度恐慌) 到 1.0 (极度贪婪) 的量化得分，精准捕捉市场拐点。

### 📉 2. 动态智能定投 (Smart DCA Optimizer)
结合用户实际持仓成本进行动态调整。**例如：假设用户的 BTC (比特币) 持仓成本基准较高，达到了 $120,000 的水平**。当市场出现回调且 AI 情绪指数判定为“极度恐慌 (错杀)”时，ClawInsight 会自动建议放大该周期的定投金额权重，加速摊薄高昂的持仓成本；反之，若在成本线下方且情绪过热，则提示暂停加仓。

### 📰 3. 创作者生态分发 (Creator Ecosystem Integration)
不仅仅是个人工具，更是自媒体的超级引擎。系统内置了“一键生成研报”的逻辑。它可以将 AI 的分析结果直接格式化为专业的公众号文章结构，非常适合拥有个人 IP（例如运营“W3 研报”或“W3 笔记”等微信公众号）的创作者，实现内容的自动化高效产出。

### 🛡️ 4. 银行级权限隔离 (Security First)
坚持“最小权限原则 (PoLP)”。只需要币安 API 的 `Read-Only` (只读) 权限即可运行完整的分析功能，绝不触碰用户的划转与提现权限。

---

## 4. ⚙️ 安装与部署 (Installation & Setup)

### 环境要求
- Python 3.9 或更高版本
- 有效的 Binance 账户 API

### 快速启动
```bash
# 1. 克隆代码库
git clone [https://github.com/你的用户名/ClawInsight-Agent.git](https://github.com/你的用户名/ClawInsight-Agent.git)
cd ClawInsight-Agent

# 2. 创建并激活虚拟环境 (推荐)
python -m venv venv
source venv/bin/activate  # Windows 用户使用 venv\Scripts\activate

# 3. 安装核心依赖
pip install -r requirements.txt

# 4. 配置环境变量
# 在根目录创建 .env 文件，并填入以下内容：
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
# 如果你所在的网络环境需要代理才能访问 Binance API，请在 .env 中增加：
# HTTP_PROXY=[http://127.0.0.1](http://127.0.0.1):你的端口
# HTTPS_PROXY=[http://127.0.0.1](http://127.0.0.1):你的端口

# 5. 运行 AI 引擎
python main.py
5. 📊 应用场景示例 (Use Cases)
运行 python main.py 后，你将获得类似如下的终端输出：

Plaintext
=============================================
🚀 欢迎使用 ClawInsight - 币安 OpenClaw 智能助手
=============================================

[*] 🧠 正在调用 OpenClaw 模型分析 BTC 的实时社区情绪...
[*] 📊 当前行情 | 代币: BTC | 价格: $64,210.50 | 情绪得分: 0.25 (恐慌)
[*] 💼 账户状态 | 历史持仓成本: $120,000.00 | 浮亏需摊薄

💡 [AI 最终决策]: 
❄️ 市场恐慌情绪蔓延，但链上大户抛压减弱。
当前价格远低于您的平均持仓成本 ($120,000)。
建议：触发智能抄底机制，将本期定投金额放大 2.0 倍，加速拉低均价。

=============================================
6. 🗺️ 发展路线图 (Roadmap)
Phase 1 (提交版本): 核心架构搭建，打通 Binance API 与基础情绪分析。

Phase 2 (Q2 2026): 引入更精细的本地大模型，支持通过 Telegram Bot 与用户进行自然语言多轮对话查询。

Phase 3 (Q3 2026): 上线一键式“研报发布器”，将深度的代币数据洞察一键分发至去中心化社交平台及 Web2 媒体矩阵。

Disclaimer: ClawInsight is an experimental AI tool built for a hackathon. It does not provide definitive financial advice. Always DYOR (Do Your Own Research) before trading.
