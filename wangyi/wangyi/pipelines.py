import json
import os

from itemadapter import ItemAdapter


class WangyiPipeline:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), '../data', 'wangyi_jobs.json')
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self.file = None
        self.items = []

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if spider.name == 'wangyi_job':
           
            adapter = ItemAdapter(item)
            self.items.append(dict(adapter))
        return item

    def close_spider(self, spider):
        if spider.name == 'wangyi_job':
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.items, f, ensure_ascii=False, indent=2)

class WangyiSimplePipeline:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), '../data', 'wangyi_simple_jobs.json')
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self.file = None
        self.items = []

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if spider.name == 'wangyi2':
            adapter = ItemAdapter(item)
            self.items.append(dict(adapter))
        return item

    def close_spider(self, spider):
        if spider.name == 'wangyi2':
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.items, f, ensure_ascii=False, indent=2)            
