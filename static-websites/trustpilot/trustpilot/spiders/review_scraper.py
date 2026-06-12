import scrapy


class ReviewScraperSpider(scrapy.Spider):
    name = "review_scraper"
    allowed_domains = ["www.trustpilot.com"]
    # start_urls = ["https://www.trustpilot.com/"]

    # def start_project(self):
    #     yield scrapy.Request(url='https://www.trustpilot.com/categories', callback=self.parse)

    async def start(self):
        # for page in range(1,25):
        yield scrapy.Request(url='https://www.trustpilot.com/categories',
                             callback=self.parse,
                             meta={
                                 'proxy':"https//swapnilmane141_gmail_com-country-any:lsvhdqdr9@gate.nodemaven.com:8080"
                             }
                             )

    def parse(self, response):
        print(response.body)

        category_link = response.xpath("//li[@class='styles_linkItem__HAUge']/a/@href").getall()

        for link in category_link:
            abs_link = response.urljoin(link)
            print(f"Processing category link: {abs_link}")
            yield scrapy.Request(url='', callback=self.parse_category, meta={
                'proxy':"https//swapnilmane141_gmail_com-country-any:lsvhdqdr9@gate.nodemaven.com:8080"

            }
            )
    def parse_category(self, response):
        print("Reached category page")
        # print(response.body)
        product_link = response.xpath('//a[@name="business-unit-card"]//@href').getall()
        for link in product_link:
            abs_link = response.urljoin(link)
            print('Processing product link:{abs_link}')
            yield scrapy.Request(url=abs_link, callback=self.parse_product, 
                                 meta=
                                 {
                                     'proxy':"https//swapnilmane141_gmail_com-country-any:lsvhdqdr9@gate.nodemaven.com:8080"

                                 })
            
            next_page = response.xpath('//a[@aria-label="Next page"]/@href').get()

            if(next_page):
                abs_next_page = response.urljoin(next_page)
                print(f"Processing next page link : {abs_next_page}")
                yield scrapy.Request(url=abs_next_page, callback=self.parse_category, meta={
                    'proxy':"https//swapnilmane141_gmail_com-country-any:lsvhdqdr9@gate.nodemaven.com:8080"

                })

    def parse_product(self, response):
        print("Reached Product page")

        review_boxes = response.xpath('//article[@data-service-review-card-paper="true"]')
        for each_review_box in review_boxes:
            review_name = each_review_box.xpath('.//*[@data-consumer-name-typography="true"]').get()
            review_stars_num = each_review_box.xpath('//div[@data-service-review-rating]/@data-service-review-rating').get()
            review_text = each_review_box.xpath('//p[@data-service-review-text-typography]/text()').get()
            review_date = each_review_box.xpath('//time[@data-service-review-date-time-ago="true"]').get()
            review_country = each_review_box.xpath('//*[@data-consumer-country-typography="true"]/text()').get()


            yield{
                'review_name': review_name,
                'review_stars_num' : review_stars_num,
                'review_text' : review_text,
                'review_date' : review_date,
                'review_country' : review_country,
                'product_url' : response.url
            }

            next_page = response.xpath('//a[@aria-label="Next page"]/@href').get()

            if(next_page):
                abs_next_page = response.urljoin(next_page)
                print(f"Processing next Product page : {abs_next_page}")
                yield scrapy.Request(url=abs_next_page, callback=self.parse_category, meta={
                    'proxy':"https//swapnilmane141_gmail_com-country-any:lsvhdqdr9@gate.nodemaven.com:8080"

                })