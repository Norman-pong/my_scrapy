from pathlib import Path
from tutorial.items import TutorialItem
import scrapy


# class ItcastSpider(scrapy.Spider):
#     name = "itcast"
#     allowed_domains = ["itcast.cn"]
#     start_urls = ["http://www.itcast.cn/channel/teacher.shtml",]

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         # filename = f"quotes-{page}.html"
#         # Path(filename).write_bytes(response.body)

#         # 获取网站标题
#         context = response.xpath('/html/head/title/text()')
#         # 提取网站标题
#         title = context.extract_first()
#         print(title)
#         pass

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml",]

    def parse(self, response):
        items = []

        for i in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = TutorialItem()
            #extract()方法返回的都是unicode字符串
            name = i.xpath("h3/text()").extract()
            title = i.xpath("h4/text()").extract()
            info = i.xpath("p/text()").extract()

            #xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)

        # 直接返回最后数据
        return items