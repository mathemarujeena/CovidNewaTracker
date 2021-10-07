from django.core.management.base import BaseCommand
from crawling.crawling.spiders.newstracker import NewsSpider
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(NewsSpider)
        process.start()

        # runner = CrawlerRunner(get_project_settings())
        # d = runner.crawl(NewsapiSpider)
        # d.addBoth(lambda _: reactor.stop())
        # reactor.run()