import scrapy
from pathlib import Path


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]

    # async def start(self):
    async def start(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        # save the  content as files
        # Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        # a = response.css(".product_pod").get()
        a = response.css(".product_pod")
        b = a.css("a")
        print('data-------->', b)