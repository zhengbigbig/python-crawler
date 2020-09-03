import re

# ^：以...开头： match方法默认是带^
# text = "hello world"
# result = re.search("world",text)
# print(result.group())


# $：以...结尾：
# text = "hello world"
# result = re.search("hello$",text)
# print(result.group())
# text = ""
# result = re.search("^$",text)
# print(result.group())


# |：匹配多个字符串或者表达式：

# text = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
# result = re.match("(http|https|ftp)://\S+",text)
# print(result.group())

# 贪婪和非贪婪：
text = 'a "witch" and her "broom" is one"'
result = re.search('".*"', text)
result2 = re.search('".*?"', text)
print(result.group())
print(result2.group())

# 案例1：提取html标签名称：
text = "<h1>这是标题</h1>"
result = re.search("<.+?>",text)
result2 = re.search("<.+>",text)
print(result.group())
print(result2.group())


# 案例2：验证一个字符是不是0-100之间的数字：
text = "101" # 0,1,88,01
result = re.match("0$|[1-9]\d?$|100$",text)
print(result.group())
