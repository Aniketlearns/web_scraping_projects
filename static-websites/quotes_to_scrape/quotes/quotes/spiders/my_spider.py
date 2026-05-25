import scrapy
from quotes.items import QuotesItem
from scrapy.loader import ItemLoader

class MySpider(scrapy.Spider):
    name ="xbot"
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quotes_list = response.xpath('//div[@class="quote"]')
        # item = QuotesItem()
        for quote in quotes_list:
            # item = QuotesItem()

            # use of loader --->
            loader = ItemLoader(item=QuotesItem(), selector=quote)
            loader.add_xpath('quote','.//span[@class="text"]/text()')
            loader.add_xpath('author','.//span/small/text()')
            tag = quote.xpath('.//div/a//text()').get()
            if tag is not None:
                loader.add_xpath('tags','.//div/a//text()')
            else:
                loader.add_value('tags', 'No Tag')

            yield loader.load_item()

            # Use of Item --->

            # item['quote']= quote.xpath('.//span[@class="text"]/text()').get()
            # item['author']= quote.xpath('.//span/small/text()').get()
            # item['tags'] = quote.xpath('.//div/a//text()').getall()

            # if item['tags']==[]:
            #     item['tags']='No Tags'
            # yield item

        nextpage = response.xpath('//li[@class="next"]/a/@href').get()
        if nextpage is not None:

            yield response.follow(nextpage, callback=self.parse)