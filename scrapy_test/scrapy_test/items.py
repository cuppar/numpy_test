# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YNZPItem(scrapy.Item):
    job_name = scrapy.Field()
    requirements = scrapy.Field()
    detail = scrapy.Field()
