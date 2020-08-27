from urllib import request

'''
urlretrieve函数：
这个函数可以方便的将网页上的一个文件保存到本地。
request.urlretrieve(url,文件名)
'''
request.urlretrieve('http://www.baidu.com/', 'baidu.html')
