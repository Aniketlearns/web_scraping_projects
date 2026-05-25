# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
# from scrapy.loader.processors import MapCompose, TakeFirst

def cut_quote(text):
    return text[:20]

class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    # quote = scrapy.Field()
    quote = scrapy.Field(
        input_processor = MapCompose(cut_quote),
        output_processor = TakeFirst()
    )
    tags = scrapy.Field()
    pass
