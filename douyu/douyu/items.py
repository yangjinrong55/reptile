# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    imageUrl = scrapy.Field()
    imageName = scrapy.Field()
    imagePath = scrapy.Field()
    #大图页面
    bigPageUrl = scrapy.Field()
    #pass
    imageName1 = scrapy.Field()
    num = scrapy.Field()
