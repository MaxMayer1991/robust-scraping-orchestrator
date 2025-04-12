import scrapy
import datetime

class CarspiderSpider(scrapy.Spider):
    name = "carspider"
    allowed_domains = ["auto.ria.com"]
    start_urls = ["https://auto.ria.com/car/used/"]

    def parse(self, response):
        cars = response.css('section.ticket-item')
        for car in cars:
            car_url = car.css("a.address::attr(href)").get()

            if car_url is not None:
                yield response.follow(car_url, callback=self.parse_car_page)

    def parse_car_page(self, response):
        price_usd = response.css("div.price_value strong::text").get()
        if price_usd:
            price_usd = price_usd.strip('\n $').replace(' ','')
            price_usd = int(price_usd)
        elif not price_usd:
            price_usd = response.css('span.data-curency::text').get()
            price_usd = str(price_usd).replace('&nbsp;','')
            price_usd = int(price_usd)
        elif not price_usd:
            price_usd = response.css('div.price_value.price_value--additional::text').get()
            price_usd = str(price_usd).split('$')[0].replace(' ','')
            price_usd = int(price_usd)

        else:
            price_usd = ''

        title = response.css("h1.head::attr(title)").get()
        if not title:
            title = ''
        otodometr = response.css("span.size18::text").get()
        if otodometr:
            otodometr = int(otodometr) * 1000
        else:
            otodometr = ''
        username = response.css("div.seller_info_name a::text").get()
        if username:
            username = str(username).strip('\n ')
        else:
            username = ''

        car_vin = response.css('span.label-vin::text').get()
        if car_vin:
            car_vin = car_vin
        elif response.css('span.vin-code::text').get():
            car_vin = response.css('span.vin-code::text').get()
        else:
            car_vin = ''

        image_count = response.css('a.show-all.link-dotted::text').get()
        if image_count:
            image_count = str(image_count).strip("Смотреть все фотографий \n")
            image_count = int(image_count)
        elif int(response.css('span.count::text').get().strip('1 из ')):
            image_count = response.css('span.count::text').get().strip('1 из ')
            image_count = int(image_count)
        else:
            image_count = ''
        yield {
            'url' : response.url,
            'title' : title,
            'price_usd' : price_usd,
            'otodometr' : otodometr,
            'username' : username if username else '',
            #phone_number = !!!! Selenium,
            'image_url' : response.css('div.photo-620x465 source::attr(srcset)').get(),
            'image_count' : image_count,
            'car_number' : str(response.css("span.state-num.ua::text").get()).strip(), #!! якщо є
            'car_vin' : car_vin,
            'datetime_found' : datetime.datetime.now()
        }