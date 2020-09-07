from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(
	executable_path="/Users/zhengzhiheng/Desktop/python-demo/python-crawler/6.动态网页爬虫/chromedriver")

driver.get("https://www.zhihu.com/signin?next=%2F")

actions = ActionChains(driver)
# 切换选项卡
target_tag = driver.find_element_by_xpath("//div[@class='SignFlow-tabs']/div[@class='SignFlow-tab']")
target_tag.click()
# 获取输入框
usernameTag = driver.find_element_by_name("username")
passwordTag = driver.find_element_by_name("password")
submitBtn = driver.find_element_by_class_name("SignFlow-submitButton")

actions.move_to_element(usernameTag)
actions.send_keys_to_element(usernameTag, "18888888888")
actions.move_to_element(passwordTag)
actions.send_keys_to_element(passwordTag, "xxxxxx")
actions.move_to_element(submitBtn)
actions.click(submitBtn)

actions.perform()
driver.quit()

'''
为什么需要行为链？
因为有些网站可能会在浏览器端做一些验证行为是否符合人类行为的反爬虫，这时候可以使用行为链来模拟人的操作，行为链有更多复杂的操作
'''
