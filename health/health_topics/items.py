# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    pass


class HealthItem(scrapy.Item):
    category = scrapy.Field()
    section = scrapy.Field()
    title = scrapy.Field()
    authors = scrapy.Field()
    reversion = scrapy.Field()
    content = scrapy.Field()
    ct = scrapy.Field()
    pass
