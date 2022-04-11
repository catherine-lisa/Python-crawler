import scrapy
from Spider.items import LianjiaItem
from scrapy.http import Request

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/dongcheng/',
                  'https://bj.lianjia.com/ershoufang/xicheng/',
                  'https://bj.lianjia.com/ershoufang/chaoyang/',
                  'https://bj.lianjia.com/ershoufang/haidian/']

    def start_requests(self):
        basic_urls = self.start_urls
        self.start_urls = []
        for urls in basic_urls:
            for i in range(1, 6):
                new_url = urls + "pg" + str(i) + '/'
                self.start_urls.append(new_url)
        for url in self.start_urls:
            yield Request(url, dont_filter=True)

    def parse(self, response):
        item = LianjiaItem()
        for each in response.xpath("/html/body/div[4]/div[1]/ul/li/div[1]"):
            item['name'] = each.xpath("div[2]/div/a[1]/text()").get().strip()
            item['price'] = each.xpath("div[6]/div[1]/span/text()").get().strip() + each.xpath("div[6]/div[1]/i[2]/text()").get().strip()
            item['area'] = each.xpath("div[3]/div/text()").get().split('|')[1].strip()
            item['unit_price'] = each.xpath("div[6]/div[2]/span/text()").get().strip()
            item['place'] = response.url.split('/')[4]
            yield (item)