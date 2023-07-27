import re

import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse, Request

from tutorial.items import HealthItem


class HealthTopicsSpider(scrapy.Spider):
    name = "health-topics"
    allowed_domains = ["www.msdmanuals.cn"]

    # start_urls = ["https://www.msdmanuals.cn/professional/health-topics"]

    def start_requests(self):
        yield scrapy.Request(url=f'https://www.msdmanuals.cn/professional/health-topics')

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        list_items = sel.css('#maincontent > section > div > div.common-one-coloumn > div > div > a')

        for list_item in list_items:
            health_item = HealthItem()
            url = response.urljoin(list_item.css('::attr(href)').extract_first().strip())
            health_item['category'] = list_item.css('::text').extract_first().strip()
            yield Request(url, callback=self.fetch_title, cb_kwargs={'item': health_item})

    # 获取标题
    def fetch_title(self, response: HtmlResponse, **kwargs):
        health_item = kwargs['item']
        sel = Selector(response)
        list_items = sel.css('#maincontent > section > div > div.medicalsection__main > ul > li')

        for list_item in list_items:
            health_item['section'] = list_item.css('div.medicalsection__caption > a::text').extract_first().strip()
            url = response.urljoin(list_item.css('div.medicalsection__caption > a::attr(href)').extract_first())
            yield Request(url, callback=self.fetch_content, cb_kwargs={'item': health_item})

    # 获取内容
    def fetch_content(self, response: HtmlResponse, **kwargs):
        health_item = kwargs['item']
        sel = Selector(response)
        head = sel.css('article > div > div > div > div > div.topic__authors--container')
        health_item['title'] = head.css('h1::text').extract_first().strip()
        authors_name = head.css('div.topic__authors-main-cont > strong > a::text').extract_first().strip()
        authors_info = head.css('div.topic__authors-main-cont > p:nth-child(3)::text').extract_first().strip()
        health_item['authors'] = authors_name + authors_info
        health_item['reversion'] = head.css('div.topic__authors-main-cont > div > div::text').extract_first().strip()
        content = sel.xpath('//article/div[@class="topic__accordion"]').extract_first()
        content = re.sub('<.*?>', "", content)
        content = re.sub('看法 进行患者培训', "", content).strip()
        health_item['content'] = content

        yield health_item