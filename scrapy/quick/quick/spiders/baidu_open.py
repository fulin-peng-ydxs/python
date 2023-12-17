import scrapy


class BaiduOpenSpider(scrapy.Spider):
    name = "baidu_open"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        print("------------")
        print(response)
