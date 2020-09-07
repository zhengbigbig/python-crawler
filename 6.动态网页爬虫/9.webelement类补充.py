from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(
	executable_path="/Users/zhengzhiheng/Desktop/python-demo/python-crawler/6.动态网页爬虫/chromedriver")

# 鼠标邮件用谷歌打开abc.html
# driver.get(
# 	r"http://localhost:63342/python-crawler/6.%E5%8A%A8%E6%80%81%E7%BD%91%E9%A1%B5%E7%88%AC%E8%99%AB/abc.html?_ijt=4vtalaelkn22aq1ajeod2t34s0")
#
# div = driver.find_element_by_id("mydiv")
# print(div.get_property("id"))
# print(div.get_property("data-name"))
# print(div.get_attribute("id"))
# print(div.get_attribute("data-name"))

driver.get("https://www.baidu.com/")
driver.save_screenshot("baidu.png")
btn = driver.find_element_by_id("su")
print(type(btn))
