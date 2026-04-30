import json

class PlannerAgent:

    def __init__(self, client, model, token_stats):
        self.client = client
        self.model = model
        self.token_stats = token_stats

    def plan(self, company: str, year: str):
        prompt = """请为""" + company + year + """年的投研报告生成任务拆解计划。

需要分析的内容：
1. 财报核心财务指标（营收、利润、毛利率、现金流）
2. 行业竞争格局
3. 技术或产品创新进展
4. 风险提示

请输出JSON格式的任务列表。"""

        result = self._call_model(prompt, "你是一个投研任务规划专家，擅长将复杂任务拆解为可执行的步骤。")

        try:
            return json.loads(result)
        except:
            return {"task_list": ["财务分析", "行业分析", "风险评估"]}

    def _call_model(self, prompt: str, system_prompt: str = ""):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.3,
            max_tokens=4096
        )

        self.token_stats["total"] += response.usage.total_tokens
        self.token_stats["steps"] += 1

        print("[Token统计] 本次: " + str(response.usage.total_tokens) + " | 累计: " + str(self.token_stats["total"]) + " | 步数: " + str(self.token_stats["steps"]))

        return response.choices[0].message.content