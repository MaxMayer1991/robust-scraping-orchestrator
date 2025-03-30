import scrapy
#import datetime

class CarspiderSpider(scrapy.Spider):
    name = "carspider"
    allowed_domains = ["auto.ria.com"]
    start_urls = ["https://auto.ria.com/car/used/"]

    def parse(self, response):
        # fetch('https://auto.ria.com/car/used/')
        cars = response.css('section.ticket-item')
        for car in cars:
            relative_url = car.css(".address::attr(href)").get()
            #car = response.css('div.ticket-status-0')
            #price = car.css("div.price_value strong::text").get()
            #otodometr = int(car.css("span.size18::text").get())*1000
            #username = car.css("h4.seller_info_name a::text").get()
            #image_url =


            title = car.css("h1.head::attr(title)").get()

            # yield{
            #     #'title' : car.css('a.address span.blue.bold::text').get().strip(),
            #     'title' : car.css('a.address span.blue.bold::text').get(),
            #     'price' : car.css(".price-ticket::attr(data-main-price)").get(),
            #     #'otodometr' : int(car.css("li.item-char.js-race::text").get().strip(' тыс. км '))*1000,
            #     'otodometr' : car.css("li.item-char.js-race::text").get(),
            #     #'car_vin' : car.css('div.base_information span.label-vin span::text').get().strip(),
            #     'car_vin' : car.css('div.base_information span.label-vin span::text').get(),
            #     'link' : car.css(".address::attr(href)").get()
            # }
        car_url = response.css("a.page-link.js-next::attr(href)").get()

        if car_url is not None:
            yield response.follow(car_url, callback=self.parse_car_page)
        pass
    def parse_car_page(self, response):
        pass