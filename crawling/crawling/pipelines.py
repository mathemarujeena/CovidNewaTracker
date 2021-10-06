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

# def clean_poster(param):
#     if param:
#         param = param[0]['path']
#     return param

# def clean_amount_reviews(param):
#     return param.strip()

# def clean_approval_percentage(param):
#     return param.strip().replace('%', '')


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        title = clean_title(item['title'])
        excerpt = clean_excerpt(item['excerpt'])
        content = clean_content(item['content'])
        author = clean_author(item['author'])
        date_published = item['date_published']
        date_created = item['date_created']
        # amount_reviews = clean_amount_reviews(item['amount_reviews'])
        # approval_percentage = clean_approval_percentage(item['approval_percentage'])

        News.objects.create(
            title=title,
            excerpt=excerpt,
            content=content,
            author=author,
            date_created=date_created,
            date_published=date_published,
        )

        return item

