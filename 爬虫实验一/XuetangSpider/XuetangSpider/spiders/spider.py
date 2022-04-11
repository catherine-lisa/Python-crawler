
import scrapy
from XuetangSpider.items import XuetangspiderItem
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
import time

class XuetangSpider(scrapy.Spider):
    name = 'xuetang'
    allowed_domains = ['www.xuetangx.com']
    start_urls = ['https://www.xuetangx.com/university/all']

    def parse(self, response):
        item = XuetangspiderItem()
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(response.url)
        driver.implicitly_wait(5)
        for i in range(1, 36):
            response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8')
            for each in response.xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/*"):
                item['school'] = each.xpath("./div[1]/p[1]/text()").get().strip()
                item['classnum'] = each.xpath("./p/text()").get().strip()
                yield (item)
            but = driver.find_element(By.CLASS_NAME, "btn-next")
            but.click()
            time.sleep(2)