import requests
import re

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}


def parse_page(page_url):
	res = requests.get(page_url, headers=headers)
	text = res.text
	house = re.findall(r'''
	<div.+?ershoufang-list".+?<a.+?js-title.+?>(.+?)</a> # 房源标题
	.+?<dd.+?dd-item.+?<span>(.+?)</span> # 获取房源的户型
	.+?<span.+?<span>(.+?)</span> # 获取房源的面积
	.+?<div.+?price.+?<span.+?>(.+?)</span> # 获取房源的价格 元/月
	''', text, re.VERBOSE | re.DOTALL)
	print(house)


def main():
	base_url = 'http://bj.ganji.com/zufang/pn{}/'
	for page in range(1, 11):
		page_url = base_url.format(page)
		parse_page(page_url)


if __name__ == '__main__':
	main()

'''
总结：
	1. 如果要让.代表所有字符，那么需要在函数后面加re.DOTALL来表示，否则不会代表\n，也就是换行。
	2. 获取数据时，都需要用非贪婪模式
	3. 如果正则写的不对，程序可能会假死，删了写的正则再逐步排错
'''
