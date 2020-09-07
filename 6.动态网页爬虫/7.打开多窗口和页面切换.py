from selenium import webdriver

driver = webdriver.Chrome(
	executable_path="/Users/zhengzhiheng/Desktop/python-demo/python-crawler/6.动态网页爬虫/chromedriver")

driver.get("https://www.baidu.com/")
driver.implicitly_wait(2)
# selenium没有专门打开新窗口的方法，是通过`window.execute_script()`来执行js
driver.execute_script("window.open('https://www.douban.com/')")
# 切换tab
driver.switch_to.window(driver.window_handles[0])

print(driver.page_source)
