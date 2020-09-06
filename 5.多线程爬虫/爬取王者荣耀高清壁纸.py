import requests
import os
import json
from urllib import parse
from urllib import request

os.chdir('/Users/zhengzhiheng/Desktop/python-demo')
download_path = './images'
if not os.path.exists(download_path):
	os.makedirs(download_path)


def extract_images(data):
	image_urls = []
	for x in range(1, 9):
		split_url = parse.unquote(data['sProdImgNo_%d' % x]).split('/')
		url = '/'.join(split_url[0:-1])
		image_urls.append(url + '/0')
	return image_urls


def parse_data_and_download(url):
	resp = requests.get(url)
	result = resp.json()
	lists = result['List']
	print(lists)
	for item in lists:
		image_urls = extract_images(item)
		name = parse.unquote(item['sProdName'])
		print(name, image_urls)
		dirpath = os.path.join('images', name)
		os.mkdir(dirpath)
		for index, image_url in enumerate(image_urls):
			request.urlretrieve(image_url, os.path.join(dirpath, "%d.jpg" % (index + 1)))


def main():
	base_url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1599298764677'
	for i in range(0, 1):
		target_url = base_url.format(i)
		parse_data_and_download(target_url)
