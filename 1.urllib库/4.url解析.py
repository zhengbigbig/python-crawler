

'''
urlparse和urlsplit函数：解析url
对url中各个组成部分进行分割，那么可以使用urlparse或者urlsplit来进行分割

urlparse和urlsplit基本一样，区别在于urlparse有params属性
'''

from urllib import parse

url = 'http://www.baidu.com/index.html;user?id=S#comment'

result = parse.urlparse(url)
# result = parse.urlsplit(url)

print(result)
print(result.scheme)
print(result.netloc)
print(result.path)
#urlparse里有params属性，而urlsplit没有这个params属性。
print(result.params)