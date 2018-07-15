import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from urllib.parse import urljoin

class GuidelineGovSpider(CrawlSpider):

    name = "guidelinegov"

    allowed_domains = [ 'www.guideline.gov' ]
    start_urls = [ 'https://www.guideline.gov' ]

    rules = [
        Rule(
            LinkExtractor(allow=(), deny=('.*/summaries/summary/.*')), 
            follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        
        #links = response.css('a::attr(href)')
        links = response.xpath('//a/@href').extract()

        for link in links:

            if '/summaries/summary/' not in link: 

                link = urljoin('https://www.guideline.gov', link)
                print("Link --> {}".format(link))

                #yield scraped_info
                #yield scrapy.http.Request(url=link, callback=self.print_link)

#    def print_link(self, link):
#        print("Link --> {}".format(link))
