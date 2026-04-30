class ParserAgent:

    def __init__(self, client, model, token_stats):
        self.client = client
        self.model = model
        self.token_stats = token_stats

    def parse(self, raw_data: str, company: str, year: str):
        prompt = """基于以下财报原始数据，提取核心财务指标并进行深度分析。

原始数据：
""" + raw_data + """

要求输出：
## 财务分析
- 营收趋势分析（同比增长率、环比增长率）
- 利润变化分析（净利润、毛利率、净利率变化）
- 现金流状况分析（经营现金流是否健康）
- 关键比率分析（ROE、负债率、流动比率）

请确保数据准确，逻辑合理。"""

        return self._call_model(prompt, "你是一个财务分析师，擅长从财报中提取关键数据并进行逻辑推理。")

    def _call_model(self, prompt: str, system_prompt: str = ""):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.3,
            max_tokens=8192
        )

        self.token_stats["total"] += response.usage.total_tokens
        self.token_stats["steps"] += 1

        print("[Token统计] 本次: " + str(response.usage.total_tokens) + " | 累计: " + str(self.token_stats["total"]) + " | 步数: " + str(self.token_stats["steps"]))

        return response.choices[0].message.content