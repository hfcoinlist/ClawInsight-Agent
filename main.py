import os
import requests
from binance.client import Client

class ClawInsightAgent:
    def __init__(self):
        """
        初始化 ClawInsight 助手，安全读取环境变量中的 API 密钥
        """
        self.api_key = os.getenv('BINANCE_API_KEY')
        self.api_secret = os.getenv('BINANCE_API_SECRET')
        
        # 如果配置了密钥则连接币安，否则仅运行离线 AI 逻辑
        if self.api_key and self.api_secret:
            self.client = Client(self.api_key, self.api_secret)
        else:
            self.client = None

    def get_openclaw_sentiment(self, symbol="BNB"):
        """
        [核心模块] 接入 OpenClaw 引擎抓取币安广场及全网情绪
        返回: 0.0 (极度恐慌) 到 1.0 (极度贪婪)
        """
        print(f"[*] 🧠 正在调用 OpenClaw 模型分析 {symbol} 的实时社区情绪...")
        # 此处为演示 Mock 数据，实际部署时将替换为 OpenClaw API
        sentiment_score = 0.75 
        return sentiment_score

    def generate_dca_strategy(self, symbol="BNB"):
        """
        结合实时现货价格与 AI 情绪，生成动态定投 (DCA) 策略
        """
        try:
            # 获取实时价格
            if self.client:
                ticker = self.client.get_symbol_ticker(symbol=f"{symbol}USDT")
                price = float(ticker['price'])
            else:
                price = 612.50 # 演示用回退价格

            # 获取 AI 情绪评分
            sentiment = self.get_openclaw_sentiment(symbol)

            print(f"[*] 📊 当前行情 | 代币: {symbol} | 价格: ${price} | 情绪得分: {sentiment}")

            # 策略大脑逻辑
            if sentiment >= 0.7:
                advice = f"🔥 市场情绪高涨 (FOMO)。建议：暂停大额买入，维持基础定投，留意回调风险。"
            elif sentiment <= 0.3:
                advice = f"❄️ 市场极度恐慌。建议：触发智能抄底机制，将本期定投金额放大 1.5 倍。"
            else:
                advice = f"⚖️ 市场情绪平稳。建议：执行标准金额定投，持续积累筹码。"
            
            return advice
            
        except Exception as e:
            return f"❌ 策略生成失败，请检查网络或 API 配置: {str(e)}"

if __name__ == "__main__":
    print("=============================================")
    print("🚀 欢迎使用 ClawInsight - 币安 OpenClaw 智能助手")
    print("=============================================\n")
    
    agent = ClawInsightAgent()
    strategy = agent.generate_dca_strategy("BNB")
    
    print(f"\n💡 [AI 最终决策]: {strategy}\n")
    print("=============================================")
