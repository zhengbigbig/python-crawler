from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/zhengzhiheng/Desktop/python-demo/python-crawler/6.动态网页爬虫/chromedriver")

# 知乎网站相关的测试代码，主要是用来验证输入框和按钮的
# driver.get("https://www.zhihu.com/signin?next=%2F")
#
# usernameTag = driver.find_element_by_name("username")
# usernameTag.send_keys("18888888888")
#
# passwordTag = driver.find_element_by_name("password")
# passwordTag.send_keys("xxxxxx")
#
# submitBtn = driver.find_element_by_class_name("SignFlow-submitButton")
# submitBtn.click()


# 豆瓣网站相关的测试代码，主要用来验证checkbox的：
# driver.get("https://accounts.douban.com/passport/login_popup?login_source=anony")
# checkbox = driver.find_element_by_name("remember")
# checkbox.click()

# 南昌航空大学测试代码，主要用来验证select的：
driver.get("http://www.nchu.edu.cn/")
# 选中标签，然后使用Select创建对象
select = Select(driver.find_element(By.ID,"ContentPlaceHolder1_dpLinkList"))
# 根据索引选择
# select.select_by_index(1)
# 根据值选择
# select.select_by_value("http://secp.jxedu.gov.cn/portal/index")
# 根据可视的文本选择
# select.select_by_visible_text("东航优惠机票1")









