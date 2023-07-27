# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoctorInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    HOSPITAL_NAME = scrapy.Field()
    DEPT_NAME = scrapy.Field()

    DOCTOR_NAME = scrapy.Field()
    DOCTOR_PIC_URL   = scrapy.Field()
    DOCTOR_SKILL = scrapy.Field()
    DOCTOR_INTRODUCTION = scrapy.Field()
    DOCTOR_QR_PATH = scrapy.Field()
    pass
