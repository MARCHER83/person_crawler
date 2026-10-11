# douban/middlewares.py
import os
import traceback
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed, signal=signals.spider_closed)
        return middleware

    def spider_opened(self, spider):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        
        # 指定 Chrome 浏览器路径
        chrome_options.binary_location = r'D:\Program Files (x86)\Chrome\App\chrome.exe'
        
        # 指定 chromedriver 路径
        driver_path = r'C:\Users\36536\.cache\selenium\chromedriver\win64\125.0.6422.141\chromedriver.exe'
        service = Service(executable_path=driver_path)

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 15)
        spider.logger.info("✅ Chrome 启动成功")
    def spider_closed(self, spider):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
            spider.logger.info("Selenium Chrome 已关闭")

    def process_request(self, request, spider):
        # 如果浏览器启动失败，直接走默认下载
        if not hasattr(self, 'driver') or self.driver is None:
            spider.logger.error("浏览器未启动，跳过 Selenium 渲染")
            return None

        if 'movie.douban.com/subject' not in request.url:
            return None

        spider.logger.info(f"Selenium 渲染: {request.url}")
        self.driver.get(request.url)

        try:
            self.wait.until(
                lambda d: 'sec.douban.com' not in d.current_url and 'subject' in d.current_url
            )
        except Exception as e:
            spider.logger.warning(f"等待跳转超时: {e}")

        body = self.driver.page_source.encode('utf-8')
        return HtmlResponse(
            url=self.driver.current_url,
            body=body,
            encoding='utf-8',
            request=request
        )