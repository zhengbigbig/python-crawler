# --coding:utf-8--
import requests
from lxml import etree
import pandas as pd

# 第一个url

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
	'Cookie': 'antipas=3451MJQ3325776RQ10d3493t56; uuid=4a47c30d-5a65-4b13-895c-b1af39dc0717; clueSourceCode=%2A%2300; ganji_uuid=7736850089831652949365; sessionid=f65eee1d-4a7f-40b9-f54d-c2a94b5bd999; lg=1; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_google%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%224a47c30d-5a65-4b13-895c-b1af39dc0717%22%2C%22ca_city%22%3A%22bj%22%2C%22sessionid%22%3A%22f65eee1d-4a7f-40b9-f54d-c2a94b5bd999%22%7D; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1598497449; lng_lat=116.31081_40.02713; gps_type=1; close_finance_popup=2020-08-27; cityDomain=www; user_city_id=-1; preTime=%7B%22last%22%3A1598497574%2C%22this%22%3A1598497412%2C%22pre%22%3A1598497412%7D; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1598497610'
}


# 获取详情页面url
def get_detail_url(url):
	resp = requests.get(url, headers=headers)
	text = resp.content.decode('utf-8')
	html = etree.HTML(text)
	li_list = html.xpath("//ul[@class='carlist clearfix js-top']/li")
	base = 'https://www.guazi.com'
	for i in li_list:
		href = base + i.xpath("./a/@href")[0]
		content = i.xpath("./a/div[1]/text()")[:2]
		yield href, content


# 解析详情页面内容
def parse_detail_page(url, count):
	with open('test.csv', 'a', encoding='utf-8') as f:
		for href, content in get_detail_url(url):
			content = content if len(content) > 0 else ['', '']
			resp = requests.get(href, headers=headers)
			text = resp.content.decode('utf-8')
			html = etree.HTML(text)
			title = html.xpath("//div[@class='product-textbox']/h2/text()")
			title = title[0].replace(r'\r\n', '').strip() if len(title) > 0 else ''
			info = html.xpath("//div[@class='product-textbox']/ul/li/span/text()")
			info = info if len(info) > 0 else ['', '']
			infos = {
				'title': title, 'card_time': content[0],
				'km': content[1], 'displacement': info[-2], 'speed_box': info[-1]
			}
			print(count, infos)
			count += 1


# save_data(infos, f)


# 保存数据
def save_data(infos, f):
	f.write('{},{},{},{},{}\n'.format(
		infos['title'], infos['card_time'], infos['km'],
		infos['displacement'], infos['speed_box']))


def main():
	count = 1
	first_url = 'https://www.guazi.com/www/buy/o{}c-1'
	for i in range(1, 51):
		parse_detail_page(first_url.format(i), count)


if __name__ == '__main__':
	main()
