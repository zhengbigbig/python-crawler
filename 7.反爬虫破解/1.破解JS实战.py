import requests
import time
import random
import hashlib

'''
对js代码进行美化后解析处理函数
'''


def main():
	word = input("请输入需要翻译的单词：")
	url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Referer": "http://fanyi.youdao.com/",
		"Cookie": "OUTFOX_SEARCH_USER_ID=180018197@10.108.160.105; JSESSIONID=aaaxEMWNp3UNN4yi-OSrx; OUTFOX_SEARCH_USER_ID_NCOO=842642437.820229; ___rl__test__cookies=1599550562586",
		"Host": "fanyi.youdao.com",
		"Origin": "http://fanyi.youdao.com"
	}
	timestamp = time.time() * 1000
	salt = str(timestamp) + str(random.randint(0, 10))
	temp = "fanyideskweb" + word + salt + "]BjuETDhU)zqSxf-=B#7m"
	sign = hashlib.md5(temp.encode("utf-8")).hexdigest()
	data = {
		"i": word,
		"from": "AUTO",
		"to": "AUTO",
		"smartresult": "dict",
		"client": "fanyideskweb",
		"salt": salt,
		"sign": sign,
		"ts": timestamp,
		"bv": "bbfff9dfb5bd0b94a08b896eebdd75fa",
		"doctype": "json",
		"version": "2.1",
		"keyfrom": "fanyi.web",
		"action": "FY_BY_REALTlME"
	}
	resp = requests.post(url, headers=headers, data=data)
	print(resp.json()["translateResult"][0][0]["tgt"])


if __name__ == '__main__':
	main()
