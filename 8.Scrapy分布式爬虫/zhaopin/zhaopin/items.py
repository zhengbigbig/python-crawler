# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
	# define the fields for your item here like:
	title = scrapy.Field()
	company = scrapy.Field()
	city = scrapy.Field()
	edu = scrapy.Field()
	work = scrapy.Field()
	desc = scrapy.Field()
