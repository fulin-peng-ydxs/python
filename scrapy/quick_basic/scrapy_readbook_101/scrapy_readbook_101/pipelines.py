# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 将数据保存到本地
class ScrapyReadbook101Pipeline:
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()


# 将数据保存到数据库
from scrapy.utils.project import get_project_settings
import pymysql


class MysqlPipeline:

    def open_spider(self, spider):
        # 加载settings文件数据库到连接配置
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWROD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        # 建立mysql数据库连接
        self.connect()

    def connect(self):
        # 建立连接
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        # 创建mysql操作对象
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print("%d/%d", item['name'], item['src'])
        sql = 'insert into book(name,src) values("{}","{}")'.format(item['name'], item['src'])
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交事务
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭数据库连接
        self.cursor.close()
        self.conn.close()
