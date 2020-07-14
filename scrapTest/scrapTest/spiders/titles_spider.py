import scrapy
#from scrapy_selenium import SeleniumRequest


class TitlesSpider(scrapy.Spider):
    name = "titles"
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI':'titles.json'
        }
    def start_requests(self):
        yield scrapy.Request(url="http://www.clarin.com",callback=self.parse)


    def parse(self, response):
        #with open("clarin.html", 'wb') as f:
        #    f.write(response.body)
        for title in response.css('h1::text,h2::text,h3::text'):
            yield {
                'title': title.get(),
            }
        content = response.css('div.on-demand::attr(data-src)').getall()
        for next in content:
            yield response.follow(next, callback=self.parse_on_demand_content)

    def parse_on_demand_content(self,response):
        for title in response.css('h1::text,h2::text,h3::text'):
            yield {
                'title': title.get(),
            }
