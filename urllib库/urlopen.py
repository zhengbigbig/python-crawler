# -- coding:utf-8 --

from urllib import request

'''
urlopen函数：
创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象来获取远程数据。
url：请求的url。
data：请求的data，如果设置了这个值，那么将变成post请求。
返回值：返回值是一个http.client.HTTPResponse对象，这个对象是一个类文件句柄对象。
有read(size)、readline、readlines以及getcode等方法。
'''
res = request.urlopen('http://baidu.com')
print(res.read())
