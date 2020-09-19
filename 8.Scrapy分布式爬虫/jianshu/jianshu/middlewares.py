from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http.response.html import HtmlResponse


class JianshuDownloaderMiddleware:
	# Not all methods need to be defined. If a method is not defined,
	# scrapy acts as if the downloader middleware does not modify the
	# passed objects.
	def __init__(self):
		self.driver = webdriver.Chrome(
			executable_path="/Users/zhengzhiheng/Desktop/python-demo/python-crawler/8.Scrapy分布式爬虫/jianshu/chromedriver")

	def process_request(self, request, spider):
		# 然后用selenium去请求
		self.driver.get(request.url)

		next_btn_xpath = "//div[@role='main']/div[position()=1]/section[last()]/div[position()=1]/div"
		WebDriverWait(self.driver, 5).until(
			EC.element_to_be_clickable((By.XPATH, next_btn_xpath))
		)

		while True:
			try:
				next_btn = self.driver.find_element_by_xpath(next_btn_xpath)
				self.driver.execute_script("arguments[0].click();", next_btn)
				# 元素若不在显示范围内，没办法直接使用.click()
			except Exception as e:
				break
		# 把selenium获得的网页数据，创建一个Response对象返回给spider
		response = HtmlResponse(request.url, body=self.driver.page_source, request=request, encoding='utf-8')
		return response

