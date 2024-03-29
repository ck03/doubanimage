# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubanimage2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    image_name = scrapy.Field()
    image_page = scrapy.Field()
    image_time = scrapy.Field()
    image_id = scrapy.Field()
    # for into mongodb
    _id = scrapy.Field()
