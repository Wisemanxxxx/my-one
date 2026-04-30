class CrawlerAgent:

    def __init__(self, client, model, token_stats):
        self.client = client
        self.model = model
        self.token_stats = token_stats

    def crawl(self, company: str, year: str):
        prompt = """请模拟从公开渠道获取""" + company + year + """年的相关财报和公告信息。

返回以下格式的内容：
1. 财报发布日期和报告期
2. 核心财务数据摘要（营收、净利润、毛利率、净利率、经营现金流）
3. 管理层讨论摘要
4. 行业相关新闻摘要"""

        return self._call_model(prompt, "你是一个数据爬取专家，擅长从财报和公告中提取结构化信息。")

    def _call_model(self, prompt: str, system_prompt: str = ""):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.5,
            max_tokens=4096
        )

        self.token_stats["total"] += response.usage.total_tokens
        self.token_stats["steps"] += 1

        print("[Token统计] 本次: " + str(response.usage.total_tokens) + " | 累计: " + str(self.token_stats["total"]) + " | 步数: " + str(self.token_stats["steps"]))

        return response.choices[0].message.content