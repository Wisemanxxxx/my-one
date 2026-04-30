class ValidatorAgent:

    def __init__(self, client, model, token_stats):
        self.client = client
        self.model = model
        self.token_stats = token_stats

    def validate(self, analysis: str):
        prompt = """请验证以下财务数据的合理性，如有异常请指出。

分析内容：
""" + analysis + """

验证项：
1. 数据格式一致性（数字格式、单位是否统一）
2. 逻辑合理性（营收增长与利润增长是否匹配，毛利率是否在合理范围内）
3. 与行业基准对比（如果数据异常，请标注）
4. 数据缺失项检查

输出格式：
- 验证通过：列出通过项
- 发现问题：列出问题及建议修正
- 综合结论：通过/需人工复核"""

        return self._call_model(prompt, "你是一个数据验证专家，擅长发现数据异常和逻辑矛盾。")

    def _call_model(self, prompt: str, system_prompt: str = ""):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.2,
            max_tokens=4096
        )

        self.token_stats["total"] += response.usage.total_tokens
        self.token_stats["steps"] += 1

        print("[Token统计] 本次: " + str(response.usage.total_tokens) + " | 累计: " + str(self.token_stats["total"]) + " | 步数: " + str(self.token_stats["steps"]))

        return response.choices[0].message.content