import re

import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse, Request

from doctor_info.items import DoctorInfoItem

class DoctorSpider(scrapy.Spider):
    name = "doctor"
    allowed_domains = ["cms.ycthealthy.com"]
    # start_urls = ["https://cms.ycthealthy.com/index.php/gzsxkyy/section/type/3/cid/262.html"]

    def start_requests(self):
        yield scrapy.Request(url=f'https://cms.ycthealthy.com/index.php/gzsxkyy/section/type/3/cid/262.html')

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        list_items = sel.css('#articleList > div.timeLine-item')

        for list_item in list_items:
            doctor_item = DoctorInfoItem()
            doctor_item['DEPT_NAME'] = list_item.css('::attr(ret-item-code)').extract_first().strip()

            url = response.urljoin(list_item.css('div > a::attr(href)').extract_first().strip())
            yield Request(url, callback=self.fetch_doctor_info, cb_kwargs={'item': doctor_item})


    def fetch_doctor_info(self, response: HtmlResponse, **kwargs):
        doctor_item = kwargs['item']
        sel = Selector(response)
        list_items = sel.css('div.expertList > div.expert-item')

        for list_item in list_items:
            img_url = list_item.css('div.expert-item-imgBox > a > img::attr(src)').extract_first().strip()

            file_path = '/file/medical/siteImgPath/'
            print(img_url)
            # scrapy.Request(url = response.urljoin(img_url),meta={'name':img_url})

            item = list_item.css('div.expert-item-con a')
            name = item.css('h3::text').extract_first().strip()

            url = response.urljoin(item.css('a::attr(href)').extract_first().strip())

            yield Request(url, callback=self.fetch_doctor_detail, cb_kwargs={'item': doctor_item, 'name': name})


    def fetch_doctor_detail(self, response: HtmlResponse, **kwargs):
          doctor_item = kwargs['item']
          sel = Selector(response)
          skill = sel.css('div.expertProfile > div.expertProfile-header > div.expertProfile-header-specialty > p:nth-child(2)').extract_first()

          intro = sel.css('div.expertProfile > div.expertProfile-con > article').extract_first()

          doctor_item['DOCTOR_NAME'] = kwargs['name']
          doctor_item['DOCTOR_SKILL'] = skill
          doctor_item['DOCTOR_INTRODUCTION'] = intro

          yield doctor_item