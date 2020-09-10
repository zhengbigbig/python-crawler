import json
# Define your item pipelines here   用来保存数据
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GswwPipeline:
	def open_spider(self, spider):
		self.fp = open("古诗文.txt", "w", encoding='utf-8')

	def process_item(self, item, spider):
		print(type(item), 'item')  # <class 'gsww.items.GswwItem'>
		self.fp.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
		# 这里必须return ，项目可能有多个pipeline，处理完这个会扔给下一个处理，如果这里中断将导致后面无法运行
		return item

	def close_spider(self, spider):
		self.fp.close()
