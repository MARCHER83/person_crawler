from scrapy_redis.spiders import RedisSpider
from douban.items import DoubanItem


class DoubanDetailSpider(RedisSpider):
    name = "douban_detail"
    allowed_domains = ["douban.com"]
    custom_settings = {
        'ITEM_PIPELINES': {
            'douban.pipelines.DoubanDetailPipeline': 301,
        }
    }
    
    def __init__(self):
        self.seen_ids = set()
        self.max_pages = 1

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://movie.douban.com/top250',
            
        }
        for i in range(0, 24, 25):
            url = f'https://movie.douban.com/top250?start={i}&filter='
            yield RedisSpider.Request(url=url, callback=self.parse_page, headers=headers)

    def parse_page(self, response):
        current_list = response.xpath('//*[@class="info"]')
        id_list = response.xpath('//*[@class="pic"]')
        
        for item, id_elem in zip(current_list, id_list):
            movie_id = id_elem.xpath('./em/text()').get()
            
            if movie_id and movie_id not in self.seen_ids:
                self.seen_ids.add(movie_id)
                
                base_data = {
                    'id': movie_id,
                    'name': item.xpath('./div[1]/a/span[1]/text()').get(),
                    'link': item.xpath('./div[1]/a/@href').get(),
                    'score': item.xpath('./div[2]/div/span[2]/text()').get(),
                    'comment': item.xpath('./div[2]/div/span[4]/text()').get(),
                    'description': ''.join(item.xpath('./div[2]/p/text()').getall()).strip(),
                    'tags': item.xpath('./div[2]/p[@class="quote"]/span/text()').get(),
                }
                
                # 关键修复：详情页请求也要带 headers
                yield RedisSpider.Request(
                    url=base_data['link'],
                    callback=self.parse_detail,
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Referer': 'https://movie.douban.com/top250',
                        'Cookie':'bid=QlRmLRuNps0; ll="118311"; _vwo_uuid_v2=D2CDC0E45CA93DA8487A9490B605B943E|2ea909ed947b059f147e958f01a6425c; ap_v=0,6.0; dbsawcv1=MTc4ODI1ODIzOEAxMDFkZGYxOGFkMWM5NTA3ZTZlYmFiZjk1YThhNTk3YzdjOGRkZDRmYTYzZmEyMzgxNjJhYzBlYTFkYTQ4OWNlQDQ3NWI4NjU4NGM4ZTZjMzFAOWYwYzEyM2U3ZTI4',
                    },
                    meta={'movie': base_data}
                )
        # 翻页逻辑
        if self.max_pages > 1:
            next_page = response.xpath('//span[@class="next"]/a/@href').get()
            if next_page:
                yield RedisSpider.Request(
                    url=response.urljoin(next_page),
                    callback=self.parse_page
                )

    def parse_detail(self, response):
        movie_id = response.meta['movie']['id']
        print(f"\n{'='*50}")
        print(f"电影ID: {movie_id}")
        print(f"状态码: {response.status}")
        print(f"最终URL: {response.url}")
        print(f"内容长度: {len(response.text)}")
        print(f"前300字: {response.text[:300]}")
        

        
        movie = response.meta['movie']
        
        storyline = response.xpath('//span[@property="v:summary"]/text()').get()
        if storyline and len(storyline) > 10:
            movie['storyline'] = storyline.strip()
        
        movie['director_detail'] = response.xpath('//div[@id="info"]/span[1]/span[2]/a/text()').get()
        
        # 关键修复：加上 /text()，否则 getall() 返回的是 HTML 标签字符串
        writers = response.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').getall()
        movie['writers'] = '/'.join(writers) if writers else None
        
        actors = response.xpath('//span/span[@class="attrs"]//span/a/text()').getall()
        movie['actors'] = '/'.join(actors[:5]) if actors else None
        
        movie['duration'] = response.xpath('//span[@property="v:runtime"]/text()').get()
        
        genres = response.xpath('//span[@property="v:genre"]/text()').getall()
        movie['genre'] = '/'.join(genres) if genres else None
        
        movie['imdb'] = response.xpath('//span[@class="pl" and contains(text(),"tt")]/following-sibling::a/text()').get()
        
        yield movie