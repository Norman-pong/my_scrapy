import openpyxl
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TutorialPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = '默沙东专业版主题'
        self.ws.append(('主题', '章节', '标题', '作者', '审查时间', '内容'))

    def close_spider(self, spider):
        self.wb.save('dist/默沙东数据.xlsx')

    def process_item(self, item, spider):
        category = item.get('category', '')
        section = item.get('section', '')
        title = item.get('title', '')
        authors = item.get('authors', '')
        reversion = item.get('reversion', '')
        content = item.get('content', '')
        self.ws.append((category, section, title, authors, reversion, content))
        return item

