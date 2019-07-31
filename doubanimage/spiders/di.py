# -*- coding: utf-8 -*-
import scrapy
from doubanimage2.items import Doubanimage2Item
from copy import deepcopy
import time
from pymongo import MongoClient


class DiSpider(scrapy.Spider):
    name = 'di'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/photos/album/1638835355']
    client = MongoClient(host="127.0.0.1", port=27017)
    collection = client["doubaneat"]["photo"]
    print("爬圖片2開始.....")
    if collection.count() > 0:
        collection.drop()
        print("已刪除Mogodb_doubaneat_photo")
    else:
        print("Mogodb_doubaneat_photo不存在")
    index = 0
    page = 1
    # stime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    stime = time.strftime("%Y%m%d", time.localtime())

    def parse(self, response):
        div_list = response.xpath("//div[@class='photolst clearfix']/div[@class='photo_wrap']")
        print(len(div_list))
        item = Doubanimage2Item()
        item["image_time"] = self.stime
        for div in div_list:
            item["image_urls"] = div.xpath("./a/img/@src").extract_first()
            item["image_name"] = div.xpath("./a/@title").extract_first() if div.xpath("./a/@title").extract_first() != "" else self.index
            item["image_page"] = self.page
            item["image_id"] = "1638835355"
            self.index += 1
            yield deepcopy(item)
            # print(item)
        self.page += 1

        # 翻頁
        page = response.xpath("//div[@class='paginator']/span[@class='next']/a")
        if len(page) > 0:
            thispage = response.xpath("//div[@class='paginator']/span[@class='thispage']/text()").extract_first()
            print(thispage)
            nextpage = int(thispage) * 18
            next_url = self.start_urls[0] + "/?m_start={}".format(nextpage)
            print(next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )