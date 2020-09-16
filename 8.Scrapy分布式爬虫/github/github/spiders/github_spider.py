import scrapy


# cookie跟踪是默认开启的

class GithubSpiderSpider(scrapy.Spider):
	name = 'github_spider'
	allowed_domains = ['github.com']
	start_urls = ['http://github.com/login']

	def parse(self, response):
		# authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").get()
		# formdata = {
		# 	"commit": "Sign in",
		# 	"authenticity_token": authenticity_token,
		# 	"login": "username",
		# 	"password": "password",
		# 	"webauthn-support": "supported"
		# }
		# yield scrapy.FormRequest("https://github.com/session", formdata=formdata, callback=self.after_login)
		# 相当于下面，将表单数据全部带过去
		yield scrapy.FormRequest.from_response(response, formdata={
			"login": "username",
			"password": "password",
		}, callback=self.after_login)

	def after_login(self, response):
		yield scrapy.Request("https://github.com/settings/profile", callback=self.visit_profile)

	def visit_profile(self, response):
		with open("github_profile.html", "w", encoding="utf-8") as fp:
			fp.write(response.text)
