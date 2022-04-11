# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from itemadapter import ItemAdapter
import csv


class LianjiaspiderPipeline:
    def open_spider(self, spider):
        try:
            self.file = open('data.csv', 'w', encoding='utf_8_sig')
            self.result = csv.writer(self.file)
            self.result.writerow(['name', 'zone', 'street', 'road', 'Room_type', 'area', 'avg_price', 'tot_price'])
        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        dict_item = ItemAdapter(item).asdict()
        self.result.writerow(dict_item.values())
        return item

    def close_spider(self, spider):
        self.file.close()