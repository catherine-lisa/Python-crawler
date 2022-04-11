# Scrapy settings for LianjiaSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'LianjiaSpider'

SPIDER_MODULES = ['LianjiaSpider.spiders']
NEWSPIDER_MODULE = 'LianjiaSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'LianjiaSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
   'LianjiaSpider.middlewares.LianjiaspiderDownloaderMiddleware': 543,
}


ITEM_PIPELINES = {
   'LianjiaSpider.pipelines.LianjiaspiderPipeline': 300,
}
