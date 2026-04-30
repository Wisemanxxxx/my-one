class AgentOrchestrator:

    def __init__(self, planner, crawler, parser, validator, writer):
        self.planner = planner
        self.crawler = crawler
        self.parser = parser
        self.validator = validator
        self.writer = writer

    def run(self, company: str, year: str):
        print("[1/5] 规划Agent: 任务拆解中...")
        plan = self.planner.plan(company, year)
        print("规划完成")
        print(plan)
        print("")

        print("[2/5] 爬取Agent: 收集财报数据中...")
        raw_data = self.crawler.crawl(company, year)
        print("爬取完成")
        print("")

        print("[3/5] 解析Agent: 财务数据分析中...")
        analysis = self.parser.parse(raw_data, company, year)
        print("分析完成")
        print("")

        print("[4/5] 验证Agent: 数据交叉验证中...")
        validation = self.validator.validate(analysis)
        print("验证完成")
        print("")

        print("[5/5] 撰写Agent: 生成研报中...")
        report = self.writer.write(company, year, analysis, validation)
        print("报告生成完成")
        print("")

        return report