import scrapy
import json
import pprint

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['nepalitimes.com']
    # start_urls = ['https://www.nepalitimes.com/']
    # start_urls = ['https://www.nepalitimes.com/latest/nepals-missing-girls/']
    start_urls = ['https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=en&source=gcsc&gss=.com&cselibv=cc267ab8871224bd&cx=bead8272edd0f2143&q=covid&safe=off&cse_tok=AJvRUv0xAj2dWUNJN-5Cj5b4CjAe:1633458820251&sort=&exp=csqr,cc&callback=google.search.cse.api17705']

    def parse(self, response):
        respe = response.text
        test = (respe[respe.find("(")+1:respe.find(");")])
        aa = json.loads(test)
        for data in aa['results']:
            print("*********************************************************************************")
            # print(data)
            # yield {
            #     'url': data['url']
            # }
            url = data['url']
            print(url)
            if url is not None:
                yield response.follow(url, callback=self.parse_url)

        # next_url = start_urls = ['https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=en&source=gcsc&gss=.com&start={}&'+
        #         'cselibv=cc267ab8871224bd&cx=bead8272edd0f2143&q=covid&safe=off&cse_tok=AJvRUv2IQVG-hrK3gHNMq1vPJW3m:1633401429938'+
        #         '&sort=&exp=csqr,cc&callback=google.search.cse.api2288'.format ]        

    def parse_url(self, response):
        # print(response)
        # print(response.css('article div.about-page-detailing h1::text').get())
        yield {
            'title': response.css('div.about-page-detailing h1::text').get(),
            'excerpt': response.css('div.about-page-detailing h5::text').get(),
            'author': response.css('span.author::text').extract()[2],
            'address': response.css('span.address::text').get(),
            'date': response.css('span.dates a::text').get(),
            'content': response.css('div.elementor-text-editor p::text').getall()
            # 'content': response.xpath('//div[@class="elementor-text-editor"/p/text()').getall()
        }

