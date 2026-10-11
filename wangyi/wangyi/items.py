# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # 基础信息
    job_id = scrapy.Field()              # id
    name = scrapy.Field()                # 职位名称
    work_type = scrapy.Field()           # workType (1=实习)
    first_post_type = scrapy.Field()    # 职位类别
    recruit_num = scrapy.Field()        # 招聘人数
    req_education = scrapy.Field()      # 学历要求
    req_work_years = scrapy.Field()     # 工作年限要求
    description = scrapy.Field()        # 职位描述
    requirement = scrapy.Field()        # 任职要求
    department = scrapy.Field()         # 所属部门 (firstDepName)
    product_name = scrapy.Field()       # 产品线名称 (productName)
    product = scrapy.Field()            # 产品代码
    work_place_list = scrapy.Field()    # 工作城市列表
    update_time = scrapy.Field()        # 更新时间戳（可转日期）

class WangyiSimpleItem(scrapy.Item):
    # 基础信息
    job_id = scrapy.Field()              # id
    name = scrapy.Field()                # 职位名称
    work_type = scrapy.Field()           # workType (1=实习)
    first_post_type = scrapy.Field()    # 职位类别
    recruit_num = scrapy.Field()        # 招聘人数
    req_education = scrapy.Field()      # 学历要求
    req_work_years = scrapy.Field()     # 工作年限要求
    description = scrapy.Field()        # 职位描述
    requirement = scrapy.Field()        # 任职要求
    department = scrapy.Field()         # 所属部门 (firstDepName)
    product_name = scrapy.Field()       # 产品线名称 (productName)
    product = scrapy.Field()            # 产品代码
    work_place_list = scrapy.Field()    # 工作城市列表
    update_time = scrapy.Field()        # 更新时间戳（可转日期）    