import json
import csv

class LianjiaPipeline:
    def open_spider(self, spider):
        try:
            self.file = open('newdata.csv', 'w', encoding='utf_8_sig')
            self.result = csv.writer(self.file)
            self.result.writerow(['area', 'name', 'price', 'unit_price', 'place'])
            self.dictionary = {'dongcheng':[], 'haidian':[], 'xicheng':[], 'chaoyang':[]}
            print("open file")
        except Exception as err:
            print(err)
    def process_item(self, item, spider):
        dict_item = dict(item)
        place = dict_item['place']
        self.dictionary[place].append(dict_item)
        # self.result.writerow(dict_item.values())
        return item
    def close_spider(self, spider):
        for i in self.dictionary:
            for j in self.dictionary[i]:
                self.result.writerow(j.values())
        self.file.close()