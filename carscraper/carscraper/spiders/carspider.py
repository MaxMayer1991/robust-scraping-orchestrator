import scrapy
from scrapy import Item

#from carscraper.carscraper.items import CarItem
class CarSpider(scrapy.Spider):
    name = "cars"
    custom_settings = {'FEED_FORMAT': {'data.csv':{'format':'csv'}}}
    def start_requests(self):
        url = ''
        yield scrapy.Request(url=url, callback=self.parse)
    start_urls = [
        'https://www.autoria.pl/pojazdy-autow/pojazdy-moczne/autobusy-moczne'
    ]
    def parse(self, response):
        products = response.css("div.product_main")

        car_item = CarItem()
        car_item['url'] = response.url
        car_item['title'] = products.css("h2.product_title a::text").get()
        car_item['price_usd'] = products.css("p.price_color::text").get()
        car_item['odometer'] = products.css("p.product_odometer::text").get()
        car_item['username'] = products.css("p.product_author a::text").get()
        car_item['phone_number'] = products.css("p.product_phone::text").get()
        car_item['image_url'] = products.css("div.product_img img::attr(src)").get()
        car_item['image_count'] = len(products.css("div.product_img img::attr(src)"))
        car_item['car_number'] = products.css("p.product_car_number::text").get()
        car_item['car_vin'] = products.css("p.product_car_vin::text").get()
        car_item['datetime_found'] = response.css("p.product_date::text").get()
        yield car_item