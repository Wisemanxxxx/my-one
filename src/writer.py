class WriterAgent:

    def __init__(self, client, model, token_stats):
        self.client = client
        self.model = model
        self.token_stats = token_stats

    def write(self, company: str, year: str, analysis: str, validation: str):
        prompt = """请为""" + company + year + """年生成一份专业投研报告。

分析内容：
""" + analysis + """

验证结果：
""" + validation + """

报告结构：
1. 执行摘要（200字内）
2. 核心财务表现
3. 战略与竞争分析
4. 风险因素
5. 投资观点与评级建议

要求：语言专业、数据准确、结构清晰。"""

        return self._call_model(prompt, "你是一个顶尖行业分析师，擅长撰写专业研报。")

    def _call_model(self, prompt: str, system_prompt: str = ""):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.4,
            max_tokens=8192
        )

        self.token_stats["total"] += response.usage.total_tokens
        self.token_stats["steps"] += 1

        print("[Token统计] 本次: " + str(response.usage.total_tokens) + " | 累计: " + str(self.token_stats["total"]) + " | 步数: " + str(self.token_stats["steps"]))

        return response.choices[0].message.content