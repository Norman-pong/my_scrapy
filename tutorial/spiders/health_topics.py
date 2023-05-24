import scrapy


class HealthTopicsSpider(scrapy.Spider):
    name = "health-topics"
    allowed_domains = ["www.msdmanuals.cn"]
    start_urls = ["https://www.msdmanuals.cn/professional/health-topics"]

    def parse(self, response):
        pass
