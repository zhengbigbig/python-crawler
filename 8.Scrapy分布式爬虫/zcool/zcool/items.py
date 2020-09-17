# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    # 保存这个Item上的图片链接
    image_urls = scrapy.Field()
    # 保存后期图片下载完成后形成的image对象保存到本地
    images = scrapy.Field()
