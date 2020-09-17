# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from . import settings
import os
import re


# 若想自定义下载逻辑则需要重写
class ImageDownloadPipeline(ImagesPipeline):

	# 将item绑定到request，使其能在file_path拿到item
	def get_media_requests(self, item, info):
		media_requests = super(ImageDownloadPipeline, self).get_media_requests(item, info)
		for media_request in media_requests:
			media_request.item = item
		return media_requests

	def file_path(self, request, response=None, info=None):
		title = request.item['title']
		# 替换文件名非法字符
		title = re.sub(r'[\\/:\*\?"<>\|]', "", title)
		origin_path = super(ImageDownloadPipeline, self).file_path(request, response, info)
		save_path = os.path.join(settings.IMAGES_STORE, title)
		if not os.path.exists(save_path):
			os.mkdir(save_path)
		image_name = origin_path.replace("full/", "")
		print(os.path.join(save_path, image_name))
		return os.path.join(save_path, image_name)
