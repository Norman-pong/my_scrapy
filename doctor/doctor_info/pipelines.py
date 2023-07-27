import openpyxl
from itemadapter import ItemAdapter


class DoctorInfoPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = '广州市胸科医院医生介绍'
        self.ws.append(('HOSPITAL_ID', 'HOSPITAL_NAME', 'DEPT_NAME', 'DOCTOR_NAME', 'DOCTOR_SKILL','DOCTOR_INTRODUCTION'))

    def close_spider(self, spider):
        self.wb.save('./dist/医生介绍.xlsx')

    def process_item(self, item, spider):
        HOSPITAL_ID = "1fac95699edc447581f1cb273b3cf39a"
        HOSPITAL_NAME = "广州市胸科医院"
        DEPT_NAME = item.get('DEPT_NAME','')
        DOCTOR_NAME = item.get('DOCTOR_NAME', '')
        DOCTOR_SKILL = item.get('DOCTOR_SKILL', '')
        DOCTOR_INTRODUCTION = item.get('DOCTOR_INTRODUCTION')

        self.ws.append((HOSPITAL_ID, HOSPITAL_NAME, DEPT_NAME, DOCTOR_NAME, DOCTOR_SKILL, DOCTOR_INTRODUCTION))
        return item


from scrapy.pipelines.images import ImagesPipeline
import  scrapy
import os


class ImgsPipLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url = item['img_src'],meta={'item':item})


    #返回图片名称即可
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        print('########',item)
        filePath = item['img_name']
        return filePath

    def item_completed(self, results, item, info):
        return item