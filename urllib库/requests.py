from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
'''
request.Request类：网络请求  可以增加请求头
'''

headers = {
	'User-Agent':
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

rq = request.Request('https://www.baidu.com/', headers=headers)

resp = request.urlopen(rq)

print(resp.read())
