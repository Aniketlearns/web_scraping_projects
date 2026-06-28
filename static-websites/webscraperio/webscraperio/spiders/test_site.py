import scrapy
from webscraperio.items import WebscraperioItem


class TestSiteSpider(scrapy.Spider):
    name = "test_site"
    allowed_domains = ["webscraper.io"]
    # start_urls = ["https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"]

    async def start(self):
        for page in range(1,6):
            yield scrapy.Request(url=f'https://webscraper.io/test-sites/e-commerce/static/computers/tablets?page={page}', callback= self.parse,
                                    )

    def parse(self, response):
        item = WebscraperioItem()
        # pass
        # return response.text[:500]
        tablet_name_list = response.xpath('//a[@itemprop="name"]//text()').getall()
        tablet_description_list = response.xpath('//p[@class="description card-text"]//text()').getall()
        tablet_price_list = response.xpath('//span[@itemprop="price"]//text()').getall()
        tablet_rating_list = response.xpath('//*[@class="ratings"]/p[2]//@data-rating').getall()
        tablet_rating_reviews_list = response.xpath('//span[@itemprop="reviewCount"]//text()').getall()
        page_link = response.xpath('//*[@property="og:url"]/@content').getall()
        # tablet_rating_reviews_list = response.xpath('//p[@class="review-count float-end"]//text()').getall()
        for tablet_name, tablet_description, tablet_price, tablet_rating, tablet_rating_reviews in zip(tablet_name_list, tablet_description_list, tablet_price_list, tablet_rating_list, tablet_rating_reviews_list):

            # item['tablet_name']= tablet_name
            # item['tablet_description']= tablet_description
            # item['tablet_price']= tablet_price
            # item['tablet_rating']= tablet_rating
            # item['tablet_rating_reviews']= tablet_rating_reviews

            # yield tablet_name.strip(), tablet_description.strip(), tablet_price.strip(), tablet_rating.strip(), tablet_rating_reviews.strip()
            yield {
                    "title": tablet_name.strip(),
                    "description": tablet_description.strip(),
                    "price": tablet_price.strip(),
                    "review_count": tablet_rating.strip(),
                    "rating": tablet_rating_reviews.strip(),
                    'page_link' : page_link
                }

            # yield scrapy.Request(callback=self.parse_article, meta={'item' : item})

    # def parse_article(self, response):
    #     item = response.meta['item']
    #     yield item


