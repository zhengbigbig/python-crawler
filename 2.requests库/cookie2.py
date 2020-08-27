import requests

'''
session:共享cookie 这里的session只是一个对象，不是web开发的session
'''
post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F'

post_data = {
	'username': '1097566154@qq.com',
	'password': 'wq15290884759.'
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# 登录
session = requests.session()
session.post(post_url, headers=headers, data=post_data)

# 访问个人网页
url = 'https://i.meishi.cc/cook.php?id=13686422'

resp = session.get(url)
print(resp.text)
