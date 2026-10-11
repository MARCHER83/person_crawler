# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# douban/items.py

class DoubanItem(scrapy.Item):
    # 列表页已有字段
    id = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    score = scrapy.Field()
    comment = scrapy.Field()
    description = scrapy.Field()   # 列表页的导演/年份/类型摘要
    tags = scrapy.Field()
    
    # 详情页新增字段
    storyline = scrapy.Field()     # 剧情简介
    director_detail = scrapy.Field()  # 导演（详情页更完整）
    writers = scrapy.Field()       # 编剧
    actors = scrapy.Field()        # 主演
    duration = scrapy.Field()      # 片长
    genre = scrapy.Field()         # 类型（更精确）
    imdb = scrapy.Field()          # IMDb链接
