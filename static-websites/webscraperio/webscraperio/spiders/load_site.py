import scrapy


class LoadSiteSpider(scrapy.Spider):
    name = "load_site"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"]

    def parse(self, response):
        tablet_name_list = response.xpath('//a[@itemprop="name"]//text()').getall()
        for table_name in tablet_name_list:

            yield {
                'table_name' :  table_name.strip(),
            }
