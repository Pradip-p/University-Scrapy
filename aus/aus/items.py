# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Course_Name = scrapy.Field()
    Category = scrapy.Field()
    Course_Website = scrapy.Field()
    Duration = scrapy.Field()
