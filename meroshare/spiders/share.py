import scrapy
from scrapy.crawler import CrawlerProcess
import time
class ShareSpider(scrapy.Spider):
    name = 'share'
    allowed_domains = ['merolagani.com']
    start_urls = ['https://merolagani.com/NewsList.aspx']

    def start_requests(self):
        yield scrapy.Request('https://merolagani.com/NewsList.aspx')

    def parse(self, response):
        websites = response.xpath('//div[@class="col-sm-6"]//div[@class="media-body"]')
        for website in websites:
            title = website.xpath('.//a/text()').get()
            date = website.xpath('.//span/text()').get()
            yield {
                'title': title,
                'date': date
            }


process = CrawlerProcess(settings={
    "FEEDS": {
        "dataset.csv": {"format": "csv"},
    },
})
process.crawl(ShareSpider)
process.start()
