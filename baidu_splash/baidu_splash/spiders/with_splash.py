import scrapy
from scrapy_splash import SplashRequest

class WithSplashSpider(scrapy.Spider):
    name = "with_splash"
    allowed_domains = ["baidu.com",'192.168.60.128']
    start_urls = ["https://www.baidu.com/s?wd=python"]

    def start_requests(self):
        yield SplashRequest(
            url = self.start_urls[0],
            callback = self.parse,
            args = {"wait": 10},
            endpoint = "render.html"
        ) 
    def parse(self, response):
        with open("with_splash.html", "wb") as f:
            f.write(response.body)