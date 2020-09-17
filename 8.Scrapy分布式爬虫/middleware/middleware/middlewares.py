# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
# 伪造user-agent
from fake_useragent import UserAgent
import random


class UserAgentDownloadMiddleware(object):
	def process_request(self, request, spider):
		ua = UserAgent(verify_ssl=False)
		user_agent_str = ua.random
		print(user_agent_str)
		request.headers['User-Agent'] = user_agent_str


class IPProxyDownloadMiddleware(object):
	PROXIES = [
		{
			'ip': "58.218.200.214",
			'port': 8122,
			'expire_time': "2020-09-17 18:03:17",
			'outip': "183.197.40.70"
		},
		{
			'ip': "58.218.200.237",
			'port': 10071,
			'expire_time': "2020-09-17 18:01:26",
			'outip': "223.78.209.80"
		}
	]

	def process_request(self, request, spider):
		proxy = random.choice(self.PROXIES)
		proxy_url = "http://" + proxy['ip'] + ':' + str(proxy['port'])
		print(proxy_url)
		request.meta['proxy'] = proxy_url
