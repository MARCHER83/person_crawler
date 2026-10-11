# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os


class DoubanPipeline:
    def __init__(self):
        self.collection_name = "douban"
        self.file_path = os.path.join(os.path.dirname(__file__), '../data', 'douban_top250_1.json')
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self.file = None
        self.items = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        item_id = adapter.get('id')
        if item_id:
            self.items[item_id] = dict(adapter)
        return item

    def close_spider(self, spider):
        sorted_items = sorted(self.items.values(), key=lambda x: int(x.get('id', 0)))
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(sorted_items, f, ensure_ascii=False, indent=2)
class DoubanDetailPipeline:
    def __init__(self):
        self.collection_name = "douban"
        self.file_path = os.path.join(os.path.dirname(__file__), '../data', 'douban_top250_2.json')
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self.file = None
        self.items = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        item_id = adapter.get('id')
        if item_id:
            self.items[item_id] = dict(adapter)
        return item

    def close_spider(self, spider):
        sorted_items = sorted(self.items.values(), key=lambda x: int(x.get('id', 0)))
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(sorted_items, f, ensure_ascii=False, indent=2)            