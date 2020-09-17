import scrapy


class MiddlewareStudySpider(scrapy.Spider):
	name = 'middleware_study'
	allowed_domains = ['httpbin.org']
	start_urls = ['http://httpbin.org/user-agent']

	def parse(self, response):
		print(response.text)
		yield scrapy.Request(self.start_urls[0], dont_filter=True)
