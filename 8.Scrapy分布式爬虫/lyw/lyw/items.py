# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LywItem(scrapy.Item):
	# define the fields for your item here like:
	title = scrapy.Field()
	pub_time = scrapy.Field()
	author = scrapy.Field()
	content = scrapy.Field()
	origin = scrapy.Field()
