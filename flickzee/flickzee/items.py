# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#
import scrapy
#
#
class FlickzeeItem(scrapy.Item):
        # define the fields for your item here like:
        Movie_Name = scrapy.Field()
        Movie_Url = scrapy.Field()
        Image_Name = scrapy.Field()

