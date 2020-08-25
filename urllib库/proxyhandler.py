from urllib import request

'''
ProxyHandler处理器（代理设置）：封ip问题

1. 代理原理：在请求目的网站之前，先请求代理服务器，
然后让代理服务器去请求目的网站，代理服务器拿到目的网站的数据后，再转发给我们的代码。

2.  http://httpbin.org：这个网站可以方便的查看http请求的一些参数。

3. 搜索快代理等，可以使用免费的一些IP
'''

# 使用代理
# 步骤
url = 'http://httpbin.org/ip'
# 1. 使用ProxyHandler,传入代理构建一个handler
handler = request.ProxyHandler({'http': '125.108.90.156:9000'})
print(1)
# 2. 使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
print(2)
# 3. 使用opener去发送一个请求
resp = opener.open(url)
print(4)
print(resp.read().decode())
