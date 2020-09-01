# --coding:utf-8--
'''
1. Tag：BeautifulSoup中所有的标签都是Tag类型，并且BeautifulSoup的对象其实本质上也是一个Tag类型。所以其实一些方法比如find、find_all并不是BeautifulSoup的，而是Tag的。
2. NavigableString：继承自python中的str，用起来就跟使用python的str是一样的。
3. BeautifulSoup：继承自Tag。用来生成BeaufifulSoup树的。对于一些查找方法，比如find、select这些，其实还是Tag的。
4. Comment：特殊的NavigableString，就是继承自NavigableString。
'''

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse">嘻嘻嘻</p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b><!--Hey, buddy. Want to buy a used parser?--></b>
"""

soup = BeautifulSoup(html, 'lxml')
# 找第一个p标签
print(soup.p)  # <p class="title" name="dromouse"></p>
print(type(soup.p))  # <class 'bs4.element.Tag'>

print(soup.p.name)  # p
print(soup.p.attrs)  # {'class': ['title'], 'name': 'dromouse'}
print(soup.p['class'])
print(soup.p.get('class'))

soup.p['class'] = 'new'
print(soup.p)  # <p class="new" name="dromouse"></p>

from bs4.element import NavigableString

print(soup.p.string)  # 嘻嘻嘻
print(type(soup.p.string))  # <class 'bs4.element.NavigableString'>

# print(type(soup))

from bs4.element import Comment

print(soup.b.string)  # Hey, buddy. Want to buy a used parser?
print(type(soup.b.string))  # <class 'bs4.element.Comment'>
