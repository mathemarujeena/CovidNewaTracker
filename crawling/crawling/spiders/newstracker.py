
import scrapy
from crawling.items import NewsItem
# from scrapy.spiders import CrawlSpider
import json
import datetime

class NewsSpider(scrapy.Spider):

    name = 'newstracker'
    allowed_domains = ['nepalitimes.com']
    start_urls = ['https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=en&source=gcsc&gss=.com&cselibv=cc267ab8871224bd&cx=bead8272edd0f2143&q=covid&safe=off&cse_tok=AJvRUv0xAj2dWUNJN-5Cj5b4CjAe:1633458820251&sort=&exp=csqr,cc&callback=google.search.cse.api17705']

    def parse(self, response):
        respe = response.text
        test = (respe[respe.find("(")+1:respe.find(");")])
        aa = json.loads(test)
        for data in aa['results']:
            print("*********************************************************************************")
            url = data['url']
            print(url)
            if url is not None:
                yield response.follow(url, callback=self.parse_url)

        # next_url = start_urls = ['https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=en&source=gcsc&gss=.com&start={}&'+
        #         'cselibv=cc267ab8871224bd&cx=bead8272edd0f2143&q=covid&safe=off&cse_tok=AJvRUv2IQVG-hrK3gHNMq1vPJW3m:1633401429938'+
        #         '&sort=&exp=csqr,cc&callback=google.search.cse.api2288'.format ]        


    def parse_url(self, response):
        news = NewsItem()
        news['title'] = response.css('div.about-page-detailing h1::text').get()
        news['excerpt'] = response.css('div.about-page-detailing h5::text').get()
        news['author'] = response.css('span.author::text').extract()[2]
        news['date_published'] = datetime.datetime.strptime(response.css('span.dates a::text').get()[1:-1], '%B %d, %Y').strftime('%Y-%m-%d')
        news['date_created'] =  datetime.datetime.today()
        news['content'] = response.css('div.elementor-text-editor p::text').getall()
        return news
       





