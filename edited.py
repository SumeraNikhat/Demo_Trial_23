# A spider application for crawling javascript based website
# It crawls only the body content using the python shell
import scrapy
class Spider1Spider(scrapy.Spider):
    name = "Spider1"

    start_urls = ["https://nextjs.org/docs/app/building-your-application/data-fetching/fetching"]

    def parse(self, response, **kwargs):
        data = response.css('h1.break-words::text').getall()
        content = response.css('p::text').getall()

        print(data)
        print(content)
