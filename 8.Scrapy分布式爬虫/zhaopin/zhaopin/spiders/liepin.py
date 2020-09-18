import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule
from ..items import ZhaopinItem


class LiepinSpider(CrawlSpider):
	name = 'liepin'
	allowed_domains = ['liepin.com']
	start_urls = ['https://www.liepin.com/zhaopin?key=python']

	rules = (
		# 详情url
		Rule(LinkExtractor(
			allow=r"https://www.liepin.com/job/\d+\.shtml.*",
			restrict_xpaths=['//ul[@class="sojob-list"]//a']),
			follow=False, callback="parse_detail"),
		# 翻页url
		Rule(LinkExtractor(
			allow=r"/zhaopin/.+curPage=\d+",
			restrict_xpaths='//div[@class="pagerbar"]//a'), follow=True),

	)

	def parse_detail(self, response):
		print(response.url)
		title = response.css('.title-info h1::text').get()
		company = response.css('.title-info h3::text').get()
		city_lst = response.css('.basic-infor span::text').getall()
		city = ''.join(city_lst).strip()
		edu = response.css('.job-qualifications span:nth-child(1)::text').get()
		work = response.css('.job-qualifications span:nth-child(2)::text').get()
		desc_lst = response.css('.content-word::text').getall()
		desc = ''.join(desc_lst).strip()
		item = ZhaopinItem(title=title, company=company, city=city, edu=edu, work=work, desc=desc)
		yield item
