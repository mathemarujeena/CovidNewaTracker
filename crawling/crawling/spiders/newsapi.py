import scrapy
from scrapy.crawler import CrawlerProcess
import copy
import json
import warnings
# from scrapy.http.request.json_request import JsonRequest
from pprint import pprint
from ..items import NewsItem
# from crawling.items import NewsItem
import urllib.parse
import datetime

class NewsapiSpider(scrapy.Spider):
    name = 'newsapi'
    allowed_domains = ['newsapi.org']
    start_urls = ['https://newsapi.org/']

    def parse(self, response):
        payload = {'apiKey':'76c34de3e1b54a61901a37b4c02f1a51','q': '_covid','language':'en','sortBy':'relevancy','pageSize':100}
        url='https://newsapi.org/v2/everything?'+urllib.parse.urlencode(payload)
        # yield scrapy.Request(url,method='GET',body=json.dumps(payload),callback=self.parse_data)
        yield scrapy.Request(url,callback=self.parse_data)

    def parse_data(self,response):
        response_json = response.json()
        articles = response_json['articles']
        for news_data in articles:
            news = NewsItem()
            news['title'] = news_data['title']
            news['url'] = news_data['url']
            news['source'] = news_data['source']['name'] if 'name' in news_data['source'] else news_data['source']
            news['excerpt'] = news_data['description']
            news['author'] = news_data['author']
            news['date_published'] = datetime.datetime.strptime(news_data['publishedAt'],"%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d')
            news['date_created'] =  datetime.datetime.today()
            news['content'] = news_data['content']
            yield news
        # pprint(response.text)  
        

          

# # main driver
# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(sc13)
#     process.start()
