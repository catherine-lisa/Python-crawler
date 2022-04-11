import scrapy

class LianjiaItem(scrapy.Item):
    name = scrapy.Field()           #楼盘名称
    price = scrapy.Field()          #总价
    area = scrapy.Field()           #平米数
    unit_price = scrapy.Field()     #单价
    place = scrapy.Field()          #地点
    pass
