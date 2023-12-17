# （1）导入selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 新增
# (2) 创建浏览器操作对象:v4.6.0或更高版本不用指定驱动程序，自己处理
# browser = webdriver.Chrome()
# 或者用此语法：
service = Service(executable_path='./driver/chromedriver')
browser = webdriver.Chrome(service=service)
# （3）访问网站
url = 'https://www.jd.com/'
browser.get(url)
# page_source获取网页源码
content = browser.page_source
print(content)

