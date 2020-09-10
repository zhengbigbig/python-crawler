import scrapy
from ..items import GswwItem

'''
实现爬取的内容，决定获取的内容，需要解析的数据等等，需要实现
'''


class GswwSpiderSpider(scrapy.Spider):
	name = 'gsww_spider'
	allowed_domains = ['gushiwen.org', 'gushiwen.cn']  # 限制只爬取对应的网址，其他的不爬取
	start_urls = ['https://www.gushiwen.org/default_1.aspx']

	def parse(self, response):
		# print(response.text)  # 运行scrapy crawl gsww_spider  后会爬取start_urls中的网站
		gsww_divs = response.xpath("//div[@class='left']/div[@class='sons']")
		print(type(gsww_divs))
		for gsww_div in gsww_divs:
			# get返回第一个文本,getall返回所有文本
			title = gsww_div.xpath(".//p/a/b/text()").get()
			if title:
				source = gsww_div.xpath(".//p[@class='source']/a/text()").getall()
				dynasty = source[0]
				author = source[1]
				content_lst = gsww_div.xpath(".//div[@class='contson']/text()").getall()
				content = "".join(content_lst).strip()
				print(title, dynasty, author, content)
				# 传入到item
				item = GswwItem(title=title, dynasty=dynasty, author=author, content=content)
				yield item  # 将数据发送给pipeline保存
		next_href = response.xpath("//div[@class='pagesright']/a[@id='amore']/@href").get()
		# 找到下一页href，然后加上域名
		if next_href:
			next_url = response.urljoin(next_href)
			print(next_url)
			request = scrapy.Request(next_url)
			yield request
