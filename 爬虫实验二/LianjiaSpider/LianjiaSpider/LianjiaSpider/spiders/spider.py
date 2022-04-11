import scrapy
from LianjiaSpider.items import LianjiaspiderItem
from scrapy.http import Request

class LianjiaSpdier(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.fang.lianjia.com']
    start_urls = ['https://bj.fang.lianjia.com/loupan/']

    def start_requests(self):
        basic_urls = self.start_urls
        self.start_urls = []
        for urls in basic_urls:
            for i in range(1, 19):
                new_url = urls + "pg" + str(i) + '/'
                self.start_urls.append(new_url)
        for url in self.start_urls:
            yield Request(url, dont_filter=True)

    def parse(self, response):
        item = LianjiaspiderItem()
        for each in response.xpath('//ul[@class="resblock-list-wrapper"]/*'):
            item.clear()
            item['name'] = each.xpath("div/div[1]/a/text()").get()
            if item['name'] != None:
                item['name'] = item['name'].strip()
            item['zone'] = each.xpath("div/div[2]/span[1]/text()").get()
            if item['zone'] != None:
                item['zone'] = item['zone'].strip()
            item['street'] = each.xpath("div/div[2]/span[2]/text()").get()
            if item['street'] != None:
                item['street'] = item['street'].strip()
            item['road'] = each.xpath("div/div[2]/a/text()").get()
            if item['road'] != None:
                item['road'] = item['road'].strip()
            #span[1]表示最小房型
            item['Room_Type'] = each.xpath("div/a/span[1]/text()").get()
            if (item['Room_Type'] != None):
                item['Room_Type'] = item['Room_Type'].strip()
            #注意后面的情况可能有多种可能，注意特判处理
            item['area'] = each.xpath("div/div[3]/span/text()").get()
            if item['area'] != None:
                item['area'] = int(item['area'].split(' ')[1].split('-')[0].strip())
            temp = each.xpath("div/div[6]/div[1]/span[2]/text()").get()
            #如果那个位置是均价：
            if temp.find('均价') != -1:
                item['avg_price'] = int(each.xpath("div/div[6]/div[1]/span[1]/text()").get().strip())
                item['tot_price'] = format(item['area'] * item['avg_price']/10000, '4f')
            #如果那个位置是总价：
            else:
                item['tot_price'] = each.xpath("div/div[6]/div[1]/span[1]/text()").get()
                item['tot_price'] = format(item['tot_price'].split('-')[0].strip(), '.4f')
                item['avg_price'] = int(item['tot_price'] * 10000 / item['area'])
            if item['name'] != None:
                yield (item)