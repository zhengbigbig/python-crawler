from scrapy import cmdline

# cmds = ['scrapy','crawl','gsww_spider']
cmdline.execute("scrapy crawl github_spider".split(" "))
