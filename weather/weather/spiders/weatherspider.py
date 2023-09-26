import scrapy
from ..items import WeatherItem #Tên của dự án + Item
import time
class SpiderBasicSpider(scrapy.Spider):
    name = "weatherspider"
    allowed_domains = ["weather.com"]
    start_urls = ["https://weather.com/"]

    def parse(self, response):
        time.sleep(5)
        city = response.xpath('//h1[@class="CurrentConditions--location--1YWj_"]/text()').get()
        temp=reviews = response.xpath('//span[@class="CurrentConditions--tempValue--MHmYY"]/text()').getall()
       # authors = response.xpath('//small[@class="author"]/text()').getall()
       # for review, author in zip(reviews, authors):
       #for review in reviews:
        
        item = WeatherItem() #Tạo 1 đối tượng chứa dữ liệu
        # temp= response.xpath('//span[@data-testid="TemperatureValue"]/text()').get()


        # item = WeatherItem()
        item["temp"]= temp
        yield item
        pass
