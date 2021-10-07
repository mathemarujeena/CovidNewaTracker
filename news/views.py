from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import NewsForm
from .models import News
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.contrib import messages
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import os
from scrapyd_api import ScrapydAPI
from scrapy.settings import Settings
from crawling.crawling.spiders import newsapi
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.core import management



def is_scraper(user):
    return user.groups.filter(name='Scraper').exists()

@login_required(login_url='/login')
@user_passes_test(is_scraper, login_url='/login')        
def news_scrape(request):
    if request.method == 'POST':
        forms = NewsForm(request.POST)
        if forms.is_valid():
            if form.cleaned_data.get('source') == 'newsapi':
                management.call_command('crawl_newsapi')
            else:
                management.call_command('crawl_nepalitimes')
            messages.success(request, f'News scrapped successfully!')
            return redirect('all-news')
    else:
        forms = NewsForm()
    context = {'forms': forms }
    return render(request, 'news/news_form.html',context)

def dashboard(request):
    total_articles = News.objects.count()
    no_of_sources = News.objects.values('source').distinct().count()
    no_of_authors = News.objects.values('author').distinct().count()
    labels = []
    datas = []

    queryset = News.objects.values('source').distinct()
    for news in queryset:
        labels.append(news['source'])
        datas.append(News.objects.filter(source=news['source']).count())
    context= {
        'total_articles':total_articles,
        'no_of_sources':no_of_sources,
        'no_of_authors': no_of_authors,
        'news':news,
        'labels': labels,
        'datas': datas
    }
    print(context)
    return render(request, 'news/dashboard.html',context)


@login_required(login_url='/login')
def search(request):

    news_ = News.objects.order_by('?') # to get unordered/shuffled list

    if request.method == 'GET':
        query= request.GET.get('search')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(content__icontains=query) | Q(author__icontains=query)

            results= News.objects.filter(lookups).distinct()

            page = request.GET.get('page', 1)
            paginator = Paginator(results, 4)
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)

            context={
                'results': results,
            }
            print(results)
            return render(request, 'news/search_result.html', context)

        else:
            return redirect('all-news')

    else:
        return redirect('all-news')

@login_required(login_url='/login')
def all_news (request):
    news = News.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 4)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        "news":news
    }
    return render(request,'news/all_news.html',context)

@login_required(login_url='/login')
def news_detail(request, slug): 

    news = News.objects.get(slug=slug) # returns only one object
    
    context = {
        'news': news
    }
    return render(request, 'news/detail_news.html', context)

@login_required(login_url='/login')
def filter_by_date(request):

    news = News.objects.order_by('?')

    if request.method == 'GET':
        query= request.GET.get('filterByDate',False)

        if query is not None:
            if query == 'today':
                today = datetime.datetime.today().strftime('%Y-%m-%d')
                news = News.objects.filter(date_published=today)
            elif query == 'latest':
                news = News.objects.order_by('-date_published')
            else:
                news = News.objects.order_by('date_published')
            page = request.GET.get('page', 1)
            paginator = Paginator(news, 4)
            try:
                news = paginator.page(page)
            except PageNotAnInteger:
                news = paginator.page(1)
            except EmptyPage:
                news = paginator.page(paginator.num_pages)
            print(news)
            context={
                'news': news
            }
            return render(request, 'news/all_news.html', context)

        else:
            return redirect('all-news')

    else:
        return redirect('all-news')


