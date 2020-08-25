from urllib import parse

'''
urlencode函数：编码
urlencode可以把字典数据转换为URL编码的数据。
'''

data = {'name': '老王', 'age': 18, 'greet': 'hello world'}

qs = parse.urlencode(data)
print(qs)  # name=%E8%80%81%E7%8E%8B&age=18&greet=hello+world
print(parse.parse_qs(qs))  # {'name': ['老王'], 'age': ['18'], 'greet': ['hello world']}

# 补充
a = '你大爷的'
print(parse.quote(a))
