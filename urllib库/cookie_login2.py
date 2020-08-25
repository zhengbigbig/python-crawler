from urllib import request
from urllib import parse
from http.cookiejar import CookieJar
from http.cookiejar import MozillaCookieJar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

'''
http.cookiejar模块：提供用于存储cookie的对象

1. CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。
整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。

2. FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。
filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据。

3. MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

4. LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。

'''

# 登录：https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F
# 个人网页https://i.meishi.cc/cook.php?id=13686422

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# 1.登录
# 1.1 创建cookiejar对象
cookiejar = CookieJar()
# 1.2 使用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3 使用上一步的创建的handler创建一个opener
opener = request.build_opener(handler)
# 1.4 使用opener发送登录请求  (账号和密码),后续这个cookie会存储到opener中

post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F'
post_data = parse.urlencode({
	'username': '1097566154@qq.com',
	'password': 'wq15290884759.'
})
req = request.Request(post_url, data=post_data.encode('utf-8'))
opener.open(req)

# 2.访问个人网页
url = 'https://i.meishi.cc/cook.php?id=13686422'
rq = request.Request(url, headers=headers)
resp = opener.open(rq)
print(resp.read().decode('utf-8'))

# cookie加载与保存
# 保存 如果在MozillaCookieJar中指定文件名，save就不用指定文件名了
cookiejar = MozillaCookieJar('cookie.txt')
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('http://www.httpbin.org/cookies/set/course/abc')

cookiejar.save(ignore_discard=True, ignore_expires=True)

# ignore_discard=True  即使cookies即将被丢弃也要保存下来
# ignore_expires=True  如果cookies已经过期也将它保存并且文件已存在时将覆盖

# 加载

cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load()
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('http://www.httpbin.org/cookies/set/course/abc')

for cookie in cookiejar:
	print(cookie)
