# Define here the models for your scraped items 提前定义好需要下载的数据字段
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GswwItem(scrapy.Item):
    # define the fields for your item here like: 提前定义好需要抓取的字段
    title = scrapy.Field()
    dynasty = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
