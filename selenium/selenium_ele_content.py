from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://www.baidu.com'
browser.get(url)
input = browser.find_element(By.ID, 'su')
# 获取标签的属性
print(input.get_attribute('class'))
# 获取标签的名字
print(input.tag_name)
# 获取元素文本
a = browser.find_element(By.LINK_TEXT, '新闻')
print(a.text)
