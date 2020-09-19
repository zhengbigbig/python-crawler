from scrapy import cmdline

# cmds = ['scrapy','crawl','gsww_spider']
cmdline.execute("scrapy crawl jianshu_spider".split(" "))
