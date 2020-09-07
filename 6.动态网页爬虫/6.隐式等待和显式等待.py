from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
	executable_path="/Users/zhengzhiheng/Desktop/python-demo/python-crawler/6.动态网页爬虫/chromedriver")

# 1. 隐式等待：
# 直接给定时间等待，若时间结束没找到则报错
# driver.get("https://www.baidu.com/")
# driver.implicitly_wait(10)
# driver.find_element_by_id("afsdasdf")

# 2. 显式等待：
# 给定时间等待，若超时则继续执行下面操作
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc")

try:
	WebDriverWait(driver, 10).until(
		EC.text_to_be_present_in_element_value((By.ID, "fromStationText"), "长沙")
	)

	WebDriverWait(driver, 10).until(
		EC.text_to_be_present_in_element_value((By.ID, "toStationText"), "北京")
	)

	btn = driver.find_element_by_id("query_ticket")
	btn.click()
except TimeoutException as e:
	driver.quit()
