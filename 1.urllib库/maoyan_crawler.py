from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
	'User-Agent':
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
url = 'https://piaofang.maoyan.com/getBoxList?date=1&isSplit=true'
rq = request.Request(url, headers=headers)
res = request.urlopen(rq)
print(res.read().decode()) # 解码
