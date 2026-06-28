import scrapy


class TestSiteSpider(scrapy.Spider):
    name = "test_site"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/"]

    def parse(self, response):
        pass
