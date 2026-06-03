import scrapy


class HockeyTeamsSpider(scrapy.Spider):
    name = "hockey_teams"
    allowed_domains = ["scrapethissite.com"]
    # start_urls = ["https://scrapethissite.com"]

    async def start(self):
        for page in range(1,25):
            # # %s Python ki string formatting ke liye use hota hai. Is code mein har loop ke page number ko URL ke andar insert karne ke liye %s use kiya gaya hai.
            # yield scrapy.Request(url='https://www.scrapethissite.com/pages/forms/?page_num=%s'%page, callback=self.parse)
            # Modern Python way :- Aajkal %s ki jagah f-string zyada use hoti hai:
            yield scrapy.Request(url=f'https://www.scrapethissite.com/pages/forms/?page_num={page}',callback=self.parse)

    def parse(self, response):
        # print(response.body)
        # team_names = response.xpath("//*[@class='name']/text()").get()
        # team_names = response.xpath("//*[@class='name']/text()").getall()
        # for each_team in team_names:
        #     yield{
        #         'Team Names': each_team.strip()
        #         # 'Team Names': each_team.replace("\n", "").replace(" ", "")
        #     }
        blocks = response.xpath("//tr[@class='team']")

        for each_block in blocks:
            team_name = each_block.xpath(".//td[@class='name']/text()").get().strip()
            team_year = each_block.xpath(".//td[@class='year']/text()").get().strip()
            team_wins = each_block.xpath(".//td[@class='wins']/text()").get().strip()
            team_losses = each_block.xpath(".//td[@class='losses']/text()").get().strip()

            yield {
                'Team Name' :team_name,
                'Team Year' :team_year,
                'Team Wins' :team_wins,
                'Team Losses' :team_losses,
                }