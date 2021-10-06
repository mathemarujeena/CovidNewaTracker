# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from news.models import News


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = News
    id = scrapy.Field()
    date_created = scrapy.Field()
    date_published = scrapy.Field()
    author = scrapy.Field()
    source = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = scrapy.Field()
    excerpt = scrapy.Field()
    content = scrapy.Field()
