import requests

'''
对于那些已经被信任的SSL证书的网站，比如https://www.baidu.com/，那么使用requests直接就可以正常的返回响应。
处理不被信任的SSL证书
'''

resp = requests.get('https://inv-veri.chinatax.gov.cn/', verify=False)
print(resp.content.decode('utf-8'))
