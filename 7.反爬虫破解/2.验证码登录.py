# 1. 因为用户名和密码和验证码的name都是随机的，所以我们要先获取网页源代码，然后提取出其中的name值。
# 2. 获取到了name和once的值以后，再通过调用https://www.v2ex.html/sigin接口，把数据通过post请求发送过去
# 3. 还需要使用云打码平台去自动识别验证码。

import requests
from lxml import etree
from urllib import request
from yundama import YDMHttp

'''
验证码类型
1. 图形验证码 (静态或者动态)
2. 拖拽验证码    需要采用机械学习和算法 较为复杂
3. 其他验证码 (12306图片选择验证码，文字点击验证码)
'''

login_url = "https://www.v2ex.com/signin"
settings_url = "https://www.v2ex.com/settings"

headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
	"referer": "https://www.v2ex.com/signin",
}

session = requests.Session()
resp = session.get(login_url, headers=headers)
html = resp.text
parser = etree.HTML(html)
inputs = parser.xpath("//form[@action='/signin']//input")
userInput = inputs[0]
passwordInput = inputs[1]
captchaInput = inputs[2]
onceInput = inputs[3]

userName = userInput.get('name')
passwordName = passwordInput.get('name')
captchaName = captchaInput.get('name')
onceValue = onceInput.get('value')

data = {
	userName: 'hynever',
	passwordName: 'abcabc',
	"once": onceValue,
	'next': '/'
}

while True:
	captcha_url = "https://www.v2ex.com/_captcha?once=" + onceValue
	imgResp = session.get(captcha_url, headers=headers)
	# 使用urlretrieve无法指定headers，导致不能下载
	with open("captcha.png", 'wb') as fp:
		fp.write(imgResp.content)

	# captchaValue = input("请输入验证码：")
	ydm = YDMHttp(username="zhiliao", password='abcabc')
	_, captchaValue = ydm.recognize_captcha("captcha.png", "3007")

	data[captchaName] = captchaValue

	loginResp = session.post(login_url, headers=headers, data=data)
	if loginResp.status_code == 302:
		break

settingsResp = session.get(settings_url, headers=headers)
print(settingsResp.text)

# 1. 云打码背后是人手工识别的，有可能识别失败，所以需要做多次的登录，直到登录成功。
# 2. v2ex一天之内只能登录10次（有待确定），如果超过了个这个次数，那么想再登录就只能更换ip地址或者等到24小时以后。
