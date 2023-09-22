import scrapy
from ..items import WeatherItem #Tên của dự án + Item

class SpiderBasicSpider(scrapy.Spider):
    name = "weatherspider"
    allowed_domains = ["weather.com"]
    start_urls = ["https://weather.com/"]

    def parse(self, response):
        temp= response.xpath('//span[class="CurrentConditions--tempValue--MHmYY"]/text()').get()
       # authors = response.xpath('//small[@class="author"]/text()').getall()
       # for review, author in zip(reviews, authors):
       #for review in reviews:
        item = WeatherItem() #Tạo 1 đối tượng chứa dữ liệu
        # temp= response.xpath('//span[@data-testid="TemperatureValue"]/text()').get()


        # item = WeatherItem()
        item["temp"]= temp
        yield item
    pass
