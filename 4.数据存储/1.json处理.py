import json

'''
## 将Python对象dump成JSON字符串：
1. dumps：把Python对象转换成JSON格式的字符串。
2. dump：把Python对象转换成JSON格式的字符串，并且还可以接收一个文件指针fp参数，可以写入到文件中。

这两个方法都有一个`ensure_ascii`参数，默认情况下这个参数的值是True，也就是说转换后的JSON字符串是只能存储ascii格式的，不能存储中文，如果想要存储成中文，那么可以将他设置为False。


## 将JSON字符串load成Python对象：
1. loads：将JSON字符串转换成Python对象。
2. load：将JSON字符串转换成Python对象，并且是直接从文件中获取JSON字符串。
'''
# python -> json
books = [{"name": "三国演义", "price": 18.8}, {"name": "水浒传", 'price': 19.9, }]

result = json.dumps(books, ensure_ascii=False)
print(result)
print(type(result))

fp = open("books.json", 'w', encoding='utf-8')
json.dump(books, fp, ensure_ascii=False)
fp.close()

# json -> python
json_str = '[{"name": "三国演义", "price": 18.8}, {"name": "水浒传", "price": 19.9}]'

print(type(json_str))
result = json.loads(json_str)
print(result)
print(type(result))

with open("books.json", 'r', encoding='utf-8') as fp:
	result = json.load(fp)
	print(result)
	print(type(result))

# Python对象->JSON字符串->Python对象
