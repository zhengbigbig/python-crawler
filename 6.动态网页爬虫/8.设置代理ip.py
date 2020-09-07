from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://110.243.16.212:9999")
driver = webdriver.Chrome(
	executable_path="/Users/zhengzhiheng/Desktop/python-demo/python-crawler/6.动态网页爬虫/chromedriver",
	options=options)

driver.get("http://httpbin.org/ip")
