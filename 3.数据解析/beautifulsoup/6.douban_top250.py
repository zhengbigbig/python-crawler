# --coding:utf-8--

import requests
from bs4 import BeautifulSoup

base_url = 'https://movie.douban.com/top250?start={}&filter='
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
	'Cookie': 'bid=sYLkg5GBefU; UM_distinctid=173dca75dba94-01056e22acb25e-31677304-384000-173dca75dbb2a8; __gads=ID=3c84fc9e6023f1ed:T=1597134784:S=ALNI_MZHnzzhqPbRWTpIwR_dMUNVbRZg9Q; __utmc=30149280; __utmz=30149280.1597134824.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ll="108288"; __utmc=223695111; __utmz=223695111.1597134861.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=ZmgGcfNkHypXQyL82IaMfivrRwPVx9jg; _vwo_uuid_v2=DEC523C3CC3FA3C520EF80B4C891C6112|1b19bc619c4574004a6b2033652fcfc9; douban-fav-remind=1; ap_v=0,6.0; _pk_ses.100001.4cf6=*; CNZZDATA1272964020=2128440914-1597132736-%7C1599010489; __utma=30149280.972159599.1597134824.1598954090.1599013386.4; __utmb=30149280.0.10.1599013386; __utma=223695111.1114705482.1597134861.1598954090.1599013386.4; __utmb=223695111.0.10.1599013386; dbcl2="188033730:EIMVyrFCbFQ"; ck=Ofxb; _pk_id.100001.4cf6=b0070892df395aea.1597134861.4.1599014061.1598956048.; push_noty_num=0; push_doumail_num=0'
}


def get_one_page_list(url):
	res = requests.get(url, headers=headers)
	content = res.content.decode('utf-8')
	soup = BeautifulSoup(content, 'lxml')

	lst = soup.select('.grid_view > li')
	for li in lst:
		yield li.find('a')['href']


def parse_detail_url(url, f):
	res = requests.get(url, headers=headers)
	content = res.content.decode('utf-8')
	soup = BeautifulSoup(content, 'lxml')

	name = soup.find('div', id='content').find('h1').stripped_strings
	name = ''.join(list(name))
	# 导演
	director = list(soup.find('div', id='info').find('span').find('span', class_='attrs').stripped_strings)
	# print(director)
	# 编剧
	screenwriter = list(soup.find('div', id='info').find_all('span')[3].find('span', class_='attrs').stripped_strings)
	# print(screenwriter)
	# 演员
	actor = list(soup.find('span', class_='actor').find('span', class_='attrs').stripped_strings)
	# print(actor)
	# 评分
	score = soup.find('strong', class_='ll rating_num').string
	print(score)
	f.write('{},{},{},{},{}\n'.format(name, ''.join(director), ''.join(screenwriter), ''.join(actor), score))


def main():
	with open('top_250.csv', 'a', encoding='utf-8') as f:
		for i in range(0, 250, 25):
			target_url = base_url.format(i)
			for detail_url in get_one_page_list(target_url):
				parse_detail_url(detail_url, f)


if __name__ == '__main__':
	main()
