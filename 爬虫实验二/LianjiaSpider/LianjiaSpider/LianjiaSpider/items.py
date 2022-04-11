# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LianjiaspiderItem(scrapy.Item):
    name = scrapy.Field()       #房屋名称
    zone = scrapy.Field()       #地区
    street = scrapy.Field()     #街道
    road = scrapy.Field()       #路
    Room_Type = scrapy.Field()  #房型
    area = scrapy.Field()       #面积
    tot_price = scrapy.Field()  #总价
    avg_price = scrapy.Field()  #均价
    pass
