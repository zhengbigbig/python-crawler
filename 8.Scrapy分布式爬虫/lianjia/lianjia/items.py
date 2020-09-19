# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
	# define the fields for your item here like:
	title = scrapy.Field()  # 标题
	city = scrapy.Field()  # 城市
	region = scrapy.Field()  # 行政区
	total_price = scrapy.Field()  # 总价
	unit_price = scrapy.Field()  # 单价
	house_type = scrapy.Field()  # 户型
	orientation = scrapy.Field()  # 朝向
	full_area = scrapy.Field()  # 总面积
	inside_area = scrapy.Field()  # 套内面积
	years = scrapy.Field()  # 年份
