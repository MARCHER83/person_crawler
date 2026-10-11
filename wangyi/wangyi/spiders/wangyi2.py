import scrapy
import json
from wangyi.items import WangyiSimpleItem   # 请根据你的项目名调整导入路径

class WangyiJobSimpleSpider(scrapy.Spider):
    name = "wangyi2"
    allowed_domains = ["hr.163.com"]
    # start_urls 不需要，用 start_requests 直接请求 API

    # 首次请求参数
    page_size = 10
    work_type = 1   # 1 表示实习
    lang = "zh"

    # 请求头，简化为必要字段，你也可以补全原脚本中的 headers
    custom_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": "https://hr.163.com/job-list.html?workType=1&lang=zh",
        "Origin": "https://hr.163.com",
    }

    def start_requests(self):
        """从第一页开始发送 POST 请求"""
        yield self.make_request(page=1)
    def make_request(self, page):
        """构建并返回一个指定页码的 POST 请求"""
        payload = {
            "currentPage": page,
            "pageSize": self.page_size,
            "workType": self.work_type,
            "lang": self.lang
        }
        return scrapy.Request(
            url="https://hr.163.com/api/hr163/position/queryPage",
            method="POST",
            body=json.dumps(payload),
            headers=self.custom_headers,
            callback=self.parse,
            meta={"page": page},
            dont_filter=True
        )
    

    def parse(self, response):
        """解析 API 返回的 JSON 数据"""
        data = json.loads(response.text)
        if data.get("code") != 200:
            self.logger.error(f"API 返回错误: {data}")
            return

        # 提取职位列表
        job_list = data.get("data", {}).get("list", [])
        for job in job_list:
            item = WangyiSimpleItem()
            item["job_id"] = job.get("id")
            item["name"] = job.get("name")
            item["work_type"] = job.get("workType")
            item["first_post_type"] = job.get("firstPostTypeName")
            item["recruit_num"] = job.get("recruitNum")
            item["req_education"] = job.get("reqEducationName")
            item["req_work_years"] = job.get("reqWorkYearsName")
            item["description"] = job.get("description")
            item["requirement"] = job.get("requirement")
            
            item["department"] = job.get("firstDepName")
            item["product_name"] = job.get("productName")
            item["product"] = job.get("product")
            item["work_place_list"] = job.get("workPlaceNameList", [])
            item["update_time"] = job.get("updateTime")
            yield item

        # # 翻页逻辑
        # total_pages = data.get("data", {}).get("pages", 1)
        # current_page = response.meta.get("page", 1)
        # self.logger.info(f"当前页: {current_page}/{total_pages}")

        # if current_page < total_pages:
        #     yield self.make_request(page=current_page + 1)