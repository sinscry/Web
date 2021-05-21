# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XinhuokolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    follower_count=scrapy.Field()
    region=scrapy.Field()
    first_type=scrapy.Field()
    first_type_score=scrapy.Field()
    media_count=scrapy.Field()
    # pass
