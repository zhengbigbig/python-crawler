# -- coding:utf-8 --

from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

'''
登录方式1：直接写入cookie进行登录
'''
url = 'https://www.zhihu.com/hot'
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
	'cookie': '_zap=f2ba4399-0373-44b3-b35f-8aac7f92dd09; d_c0="ADBbdLRBnBGPTsAnG1LjbfvU-UcTx87YUGI=|1595323983"; _ga=GA1.2.1914720822.1595324027; UM_distinctid=17370b8d0714e9-0fc2d1c2055372-15366651-384000-17370b8d072cee; _xsrf=5024e29a-c33d-4ab1-bc12-fa8c5b0a0e20; z_c0="2|1:0|10:1597655614|4:z_c0|92:Mi4xQ0Jjd0NBQUFBQUFBTUZ0MHRFR2NFU1lBQUFCZ0FsVk5QcGduWUFBOVZkdkNaYUMzUHAtaFhVT24yUm9SOFRLMGt3|46a9d56f15fe065e1b56effe7d7520c8a0d476892701b1c048e62e621a452756"; capsion_ticket="2|1:0|10:1597657119|14:capsion_ticket|44:NzBkOGUwMmRkMzE1NDY0YmIxMTYxZTM5MmUxMGY5NjI=|94f4bba8a3aa43c115b58e99b93cb6d08cfb0212a1245862f30ac1bbe0549f56"; q_c1=1ecb3e9397f34a1097c43f1d562f0e8c|1597735772000|1597735772000; _gid=GA1.2.530034617.1598343300; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1597918247,1597918453,1598241786,1598343301; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1598343301; CNZZDATA1272960301=648086986-1596507322-https%253A%252F%252Fwww.google.com.hk%252F%7C1598341954; SESSIONID=w5czyNU5sx1NSGIl87Nw7GiS5HxPbXP2Ui5GpAHifU3; JOID=W14QB005OMT4oq64PTQIk4MeTxUgQQ6mgNTv7glFT_a38-b-Ulfyg6qioro-1s4fwXKKOO1jpbCWKXmdmT6J34M=; osd=V1ERBk41N8X5oaK3PDULn4wfThYsTg-ng9jg7whGQ_m28uXyXVbzgKato7s92sEewHGGN-xipryZKHielTGI3oA=; tst=h; KLBRSID=d017ffedd50a8c265f0e648afe355952|1598343271|1598343262; tshl='
}
rq = request.Request(url, headers=headers)
res = request.urlopen(rq)
print(res.read().decode('utf-8'))
