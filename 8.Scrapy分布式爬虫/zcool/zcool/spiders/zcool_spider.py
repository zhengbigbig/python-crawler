import scrapy
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ImageDownloadItem


class ZcoolSpiderSpider(CrawlSpider):
	name = 'zcool_spider'
	allowed_domains = ['zcool.com.cn']
	start_urls = ['http://zcool.com.cn/']

	rules = (
		# 翻页url
		Rule(LinkExtractor(allow=r"/?p=\d+#tab_anchor"), follow=True),
		# 详情url
		Rule(LinkExtractor(allow=r"/work/.+.html"), follow=False, callback="parse_detail")
	)

	def parse_detail(self, response):
		image_urls = response.xpath("//div[contains(@class,'work-show-box')]//img/@src").getall()
		title = "".join(response.xpath("//div[@class='details-contitle-box']/h2/text()").getall()).strip()
		item = ImageDownloadItem(title=title, image_urls=image_urls)
		yield item
