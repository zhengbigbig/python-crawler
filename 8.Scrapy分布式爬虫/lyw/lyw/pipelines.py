# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# twisted 异步
from twisted.enterprise import adbapi

'''
1、使用twisted.enterprise.adbapi来创建连接池
2、使用runInteraction来运行插入sql语句的函数
3、在插入sql语句的函数中，第一个非self的参数就是cursor对象，使用这个对象执行sql语句。
'''


# 异步操作数据库
class LywPipeline:
	def __init__(self, mysql_config):
		self.dbPool = adbapi.ConnectionPool(
			mysql_config['DRIVER'],
			host=mysql_config['HOST'],
			port=mysql_config['PORT'],
			user=mysql_config['USER'],
			password=mysql_config['PASSWORD'],
			db=mysql_config['DATABASE'],
			charset='utf8'
		)

	@classmethod
	def from_crawler(cls, crawler):
		# 只要重写了from_crawler方法，那么以后创建对象的时候，就会调用这个方法来获取pipeline对象
		# 原本应该是LywPipeline()，现在变成LywPipeline.from_crawler(crawler)
		mysql_config = crawler.settings['MYSQL_CONFIG']
		return cls(mysql_config)

	def process_item(self, item, spider):
		# 运行插入sql语句的函数
		result = self.dbPool.runInteraction(self.insert_item, item)
		result.addErrback(self.insert_error)
		return item

	def insert_item(self, cursor, item):
		sql = '''insert into article (title, author, pub_time, content,origin)
				values (%s,%s,%s,%s,%s);
		'''
		args = (item['title'], item['author'], item['pub_time'], item['content'], item['origin'])
		# 执行sql语句
		cursor.execute(sql, args)

	def insert_error(self, failure):
		print('=' * 30)
		print(failure)
		print('=' * 30)
