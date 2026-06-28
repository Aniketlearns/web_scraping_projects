import scrapy


class IplauctionSpider(scrapy.Spider):
    name = "iplauction"
    allowed_domains = ["www.iplt20.com"]
    start_urls = ["https://www.iplt20.com/auction"]

    async def start(self):
        yield scrapy.Request(url='https://www.iplt20.com/auction',
                             method= 'get',
                            # cookies = {
                            #     'AWSALB': 'rBkjMx+fkGw8JhtenIKOGzEdTLahf6ATR7LN9nls4kFhCCFP7+PL9G45m3Q+xpqg5JnYYg/QfTnVVTb491b6J3wWLRe5qMCHRcMbypKWpW1h7PjtSmMM5WJJglVf',
                            #     'AWSALBCORS': 'rBkjMx+fkGw8JhtenIKOGzEdTLahf6ATR7LN9nls4kFhCCFP7+PL9G45m3Q+xpqg5JnYYg/QfTnVVTb491b6J3wWLRe5qMCHRcMbypKWpW1h7PjtSmMM5WJJglVf',
                            #     'laravel_session': 'eyJpdiI6IkFVUW1LRkNjTm9Yd2JCTUhQamZkZ2c9PSIsInZhbHVlIjoiNGJjbWxoV2V4UHRESE5DejVnQUdacC9GaG1MUlRXK0pOblNFS2dhdmZpWGFhRHdRMlV3N0ZhNkdNN2ZpOW1rYmpCQkZDeEd2cjB5bU9DSTFmcmVZSVR1UkJBVFptYlg5aXJJVEM3bHZ0cUlTem5UcUw1WTJPMzRBM2pDajJqWUYiLCJtYWMiOiI1ZWNhZWU0MWE1OGJjNmFkNzYyYmZmOTU2ZDRmNWU5Nzk3NGU4Y2RlMzE0OGNjODgwNDkwMDU0YmVhZTdlZjI1IiwidGFnIjoiIn0%3D',
                            # },
                            # headers = {
                            #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                            #     'accept-language': 'en-GB,en;q=0.8',
                            #     'cache-control': 'max-age=0',
                            #     'priority': 'u=0, i',
                            #     'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                            #     'sec-ch-ua-mobile': '?0',
                            #     'sec-ch-ua-platform': '"macOS"',
                            #     'sec-fetch-dest': 'document',
                            #     'sec-fetch-mode': 'navigate',
                            #     'sec-fetch-site': 'none',
                            #     'sec-fetch-user': '?1',
                            #     'sec-gpc': '1',
                            #     'upgrade-insecure-requests': '1',
                            #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                            #     # 'cookie': 'AWSALB=rBkjMx+fkGw8JhtenIKOGzEdTLahf6ATR7LN9nls4kFhCCFP7+PL9G45m3Q+xpqg5JnYYg/QfTnVVTb491b6J3wWLRe5qMCHRcMbypKWpW1h7PjtSmMM5WJJglVf; AWSALBCORS=rBkjMx+fkGw8JhtenIKOGzEdTLahf6ATR7LN9nls4kFhCCFP7+PL9G45m3Q+xpqg5JnYYg/QfTnVVTb491b6J3wWLRe5qMCHRcMbypKWpW1h7PjtSmMM5WJJglVf; laravel_session=eyJpdiI6IkFVUW1LRkNjTm9Yd2JCTUhQamZkZ2c9PSIsInZhbHVlIjoiNGJjbWxoV2V4UHRESE5DejVnQUdacC9GaG1MUlRXK0pOblNFS2dhdmZpWGFhRHdRMlV3N0ZhNkdNN2ZpOW1rYmpCQkZDeEd2cjB5bU9DSTFmcmVZSVR1UkJBVFptYlg5aXJJVEM3bHZ0cUlTem5UcUw1WTJPMzRBM2pDajJqWUYiLCJtYWMiOiI1ZWNhZWU0MWE1OGJjNmFkNzYyYmZmOTU2ZDRmNWU5Nzk3NGU4Y2RlMzE0OGNjODgwNDkwMDU0YmVhZTdlZjI1IiwidGFnIjoiIn0%3D',
                            # },

                            headers={
                            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36",
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                            "Accept-Language": "en-US,en;q=0.9",
                            # "Referer": "https://www.google.com/",
                            "Referer": "https://www.iplt20.com/auction",
                            
                            },
                            callback=self.parse,
                            )

    def parse(self, response):
        # serial_num_list = response.xpath('//table[@class="ih-td-tab w-100 auction-tbl"]/tbody[@id="pointsdata"]//tr/td[1]//text()').getall()
        # team_logo_list = response.xpath('//table[@class="ih-td-tab w-100 auction-tbl"]/tbody[@id="pointsdata"]//tr/td[2]/div/div/img/@src').getall()
        # player_list = response.xpath('//table[@class="ih-td-tab w-100 auction-tbl"]/tbody[@id="pointsdata"]//tr/td[3]/text()').getall()
        # Base_Price_list = response.xpath('//table[@class="ih-td-tab w-100 auction-tbl"]/tbody[@id="pointsdata"]//tr/td[4]/text()').getall()
        # Winning_Bid_list = response.xpath('//table[@class="ih-td-tab w-100 auction-tbl"]/tbody[@id="pointsdata"]//tr/td[4]/text()').getall()
        player_name_list = response.xpath('//table[@class="ih-td-tab w-100 auction-tbl"]/tbody[@id="pointsdata"]//tr/td[1]//text()').getall()



        for player_name in player_name_list:
            player_name = player_name.strip()

            if not player_name:
                continue   # empty records skip kar do

            # if player_name == "":
            #     break
        # for serial_num, team_logo, player, Base_Price, Winning_Bid in zip(serial_num_list, team_logo_list, player_list, Base_Price_list, Winning_Bid_list):

            yield {
                'player_name' : player_name.strip().replace("", ''),
                # 'serial_num' : serial_num.strip(),
                #    'team_logo' : team_logo.strip(),
                #    'player' : player.strip(),
                #    'Base_Price' :Base_Price.strip(),
                #    'Winning_Bid' : Winning_Bid.strip(),
                   }


# import scrapy


# class IplauctionSpider(scrapy.Spider):
#     name = "iplauction"
#     allowed_domains = ["www.iplt20.com"]

#     custom_settings = {
#         "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36",
#         "DEFAULT_REQUEST_HEADERS": {
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#             "Accept-Language": "en-US,en;q=0.9",
#             "Referer": "https://www.google.com/",
#         },
#     }

#     def start_requests(self):
#         yield scrapy.Request(
#             url="https://www.iplt20.com/auction",
#             callback=self.parse,
#             dont_filter=True,
#         )

#     def parse(self, response):
#         self.logger.info(f"Status: {response.status}")

#         rows = response.xpath(
#             '//*[@class="ih-td-tab w-100 auction-tbl dataTable no-footer"]/tbody/tr'
#         )

#         if not rows:
#             yield {
#                 "status": response.status,
#                 "message": "No table rows found",
#                 "html_preview": response.text[:1000],
#             }
#             return

#         for row in rows:
#             data = row.xpath(".//td//text()").getall()
#             data = [x.strip() for x in data if x.strip()]

#             yield {
#                 "player_data": data
#             }