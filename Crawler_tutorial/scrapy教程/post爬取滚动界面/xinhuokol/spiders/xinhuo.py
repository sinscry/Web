import scrapy
from xinhuokol.items import XinhuokolItem


class XinhuoSpider(scrapy.Spider):
    name = 'xinhuo'
    allowed_domains = ['www.xinhuokol.com']
    start_urls = ['https://www.xinhuokol.com/instagram/search']

    def parse(self, response):
        node_list = response.xpath("//div[@class='el-card__body']")
        items = []
        for node in node_list:
            item = XinhuokolItem()
            name_region = node.xpath("./div[@class='bloger-baseinfo']/div/a/span/text()").extract()
            item['name'] = name_region[0]
            item['region'] = name_region[1]

            first_tpye = node.xpath("./div[@class='bloger-baseinfo']/div/span/span/text()").extract()
            item['first_type'] = first_tpye[0]
            item['first_type_score'] = first_tpye[1]

            fans_photo = node.xpath("./div[@class='bloger-analysis']/div/p/text()").extract()
            item['follower_count'] = fans_photo[1]
            item['media_count'] =fans_photo[3]

            items.append(item)
        print(len(items))
        return items
        pass
