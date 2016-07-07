# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class DbSpiderItem(scrapy.Item):
    book_name = Field()
    book_star = Field()
    book_rating = Field()
    book_eval = Field()
    book_author = Field()
    book_pulish = Field()
    book_price = Field()
