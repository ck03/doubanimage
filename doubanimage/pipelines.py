# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import json
from pymongo import MongoClient
from copy import deepcopy


class Doubanimage2Pipeline(object):
    result_list = []
    result_dict = {}
    client = MongoClient(host="127.0.0.1", port=27017)
    collection = client["doubaneat"]["photo"]

    def process_item(self, item, spider):
        # print(item)
        item_copy = deepcopy(item)
        self.result_list.append(item)
        self.collection.insert(item_copy)
        return item

    def close_spider(self, spider):
        self.result_dict["Result"] = self.result_list
        # print(self.result_dict)
        print(type(self.result_dict))
        # XXX is not JSON serializable會報這個錯,加了eval(repr(self.result_dict))就不會了
        with open("罪恶花园导游的相册.json", "w",
                  encoding="utf-8") as f:
            f.write(json.dumps(eval(repr(self.result_dict)), ensure_ascii=False, indent=2))

        print("爬圖片2爬蟲結束.....")


class DoubanImgDownloadPipeline(ImagesPipeline):
    # default_headers = {
    #     'accept': 'image/webp,image/*,*/*;q=0.8',
    #     'accept-encoding': 'gzip, deflate, sdch, br',
    #     'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
    #     'cookie': 'bid=yQdC/AzTaCw',
    #     'referer': 'https://www.douban.com/photos/photo/2370443040/',
    #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    # }

    # 在這裡下載圖片到本地
    def get_media_requests(self, item, info):
        # item是一個字典==>{'image_urls': ['圖片連結','圖片連結','圖片連結',...]}
        # self.default_headers['referer'] = item['image_urls']
        # yield Request(item['image_urls'], headers=self.default_headers)
        yield Request(item['image_urls'])

    def item_completed(self, results, item, info):
        # print(results)
        # image_paths = [x['path'] for ok, x in results if ok]
        image_paths = results[0][1]["path"]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
