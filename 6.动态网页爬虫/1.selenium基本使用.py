from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/zhengzhiheng/Desktop/python-demo/python-crawler/6.动态网页爬虫/chromedriver")

driver.get("https://www.baidu.com")

time.sleep(4)

# close 是关闭当前网页，若关闭的就是最后一个，直接关闭浏览器
# quit是直接关闭整个浏览器
driver.quit()
