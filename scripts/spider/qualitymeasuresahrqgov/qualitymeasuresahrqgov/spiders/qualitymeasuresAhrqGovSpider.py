import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from urllib.parse import urljoin

class qualitymeasuresAhrqGovSpider(CrawlSpider):

    name = "qualitymeasuresahrqgov"

    allowed_domains = [ 'qualitymeasures.ahrq.gov' ]
    start_urls = [ 'https://qualitymeasures.ahrq.gov' ]

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

                link = urljoin('https://qualitymeasures.ahrq.gov', link)
                print("Link --> {}".format(link))

                #yield scraped_info
                #yield scrapy.http.Request(url=link, callback=self.print_link)

#    def print_link(self, link):
#        print("Link --> {}".format(link))
