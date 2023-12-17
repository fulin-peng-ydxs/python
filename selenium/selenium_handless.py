from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # path是你自己的chrome浏览器的驱动路径
    # path = r'./driver/chromedriver'
    # chrome_options.binary_location = path
    return webdriver.Chrome(options=chrome_options)

browser = share_browser()
browser.get('https://www.baidu.com')
# 页面快照
browser.save_screenshot('baidu.png')
