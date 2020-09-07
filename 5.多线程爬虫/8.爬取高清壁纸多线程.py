from typing import Optional, Callable, Any, Iterable, Mapping

import requests
import os
from urllib import parse
from urllib import request
import threading
import queue

os.chdir('/Users/zhengzhiheng/Desktop/python-demo')
download_path = './images'
if not os.path.exists(download_path):
	os.makedirs(download_path)

headers = {
	'referer': 'https://pvp.qq.com/web201605/wallpaper.shtml',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}


class Producer(threading.Thread):

	def __init__(self, page_queue, image_queue, *args, **kwargs):
		super(Producer, self).__init__(*args, **kwargs)
		self.page_queue = page_queue
		self.image_queue = image_queue

	@staticmethod
	def extract_images(data):
		image_urls = []
		for x in range(1, 9):
			split_url = parse.unquote(data['sProdImgNo_%d' % x]).split('/')
			url = '/'.join(split_url[0:-1])
			image_urls.append(url + '/0')
		return image_urls

	def run(self):
		while not self.page_queue.empty():
			# 获取json数据
			page_url = self.page_queue.get()
			resp = requests.get(page_url, headers=headers)
			result = resp.json()
			lists = result['List']
			# 将获取到的url及信息解析放入队列
			for item in lists:
				image_urls = self.extract_images(item)
				name = parse.unquote(item['sProdName']).replace("1:1", "").strip()
				dirpath = os.path.join('images', name)

				if not os.path.exists(dirpath):
					os.makedirs(dirpath)
				for index, image_url in enumerate(image_urls):
					self.image_queue.put({
						'image_url': image_url,
						'image_path': os.path.join(dirpath, "%d.jpg" % (index + 1))
					})


class Consumer(threading.Thread):
	def __init__(self, image_queue, *args, **kwargs):
		super(Consumer, self).__init__(*args, **kwargs)
		self.image_queue = image_queue

	def run(self):
		while True:
			try:
				# 设置timeout，如果超时10s没数据就会超时报异常
				imgae_obj = self.image_queue.get(timeout=10)
				image_url = imgae_obj.get('image_url')
				image_path = imgae_obj.get('image_path')
				try:
					request.urlretrieve(image_url, image_path)
					print(image_path, '下载完成')
				except:
					print('下载失败')
			except:
				break


def main():
	page_queue = queue.Queue(24)
	image_queue = queue.Queue(1000)

	base_url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1599298764677'
	for i in range(0, 24):
		target_url = base_url.format(i)
		page_queue.put(target_url)
	for x in range(3):
		th = Producer(page_queue, image_queue, name="生产者%d号" % x)
		th.start()
	for x in range(3):
		th = Consumer(image_queue, name="消费者%d号" % x)
		th.start()


if __name__ == '__main__':
	main()
