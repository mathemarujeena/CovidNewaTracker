# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from news.models import News

def clean_title(param):
    return param.strip()

def clean_content(param):
    return ' '.join(param).strip().replace('\n','')

def clean_excerpt(param):
    param = param.strip().replace('\n','')
    return param

def clean_author(param):
    param = param.strip()
    return param


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        title = clean_title(item['title'])
        excerpt = clean_excerpt(item['excerpt'])
        content = clean_content(item['content'])
        author = clean_author(item['author'])
        date_published = item['date_published']
        date_created = item['date_created']
        source = item['source']
        url = item['url']

        News.objects.create(
            title=title,
            excerpt=excerpt,
            content=content,
            author=author,
            date_created=date_created,
            date_published=date_published,
            source= source,
            url = url
        )

        return item

