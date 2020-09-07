from selenium import webdriver

'''
find_element_by_id：根据id来查找某个元素。
find_element_by_class_name：根据类名查找元素。
find_element_by_name：根据name属性的值来查找元素。
find_element_by_tag_name：根据标签名来查找元素。
find_element_by_xpath：根据xpath语法来获取元素。
find_element_by_css_selector：根据css选择器选择元素。

要注意，find_element是获取第一个满足条件的元素。find_elements是获取所有满足条件的元素。
'''

driver = webdriver.Chrome(executable_path="/Users/zhengzhiheng/Desktop/python-demo/python-crawler/6.动态网页爬虫/chromedriver")

driver.get("https://www.baidu.com")

inputTag = driver.find_element_by_id("kw")
inputTags = driver.find_elements_by_class_name("s_ipt")[0]
print(inputTags)
inputTag = driver.find_element_by_name("wd")
inputTag = driver.find_element_by_tag_name("input")
inputTag = driver.find_element_by_xpath("//input[@id='kw']")
inputTag = driver.find_element_by_css_selector("#form #kw")
inputTag.send_keys("python")
