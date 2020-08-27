import requests

# 使用代理
# 只要在请求的方法中（比如get或者post）传递proxies参数就可以了。

proxy = {
	'http': '60.167.134.95:9999'
}
url = 'http://www.httpbin.org/ip'
resp = requests.get(url, proxies=proxy)
print(resp.text)
