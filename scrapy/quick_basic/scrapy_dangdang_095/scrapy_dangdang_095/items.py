# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang095Item(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义item数据项：作为在管道中的数据信息的传递载体，
    # 每个字段都是 scrapy.Field() 类型的实例

    # 图片
    src = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()

