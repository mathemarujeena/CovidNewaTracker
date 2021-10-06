from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import NewsForm
from .models import News
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
import datetime


def index(request):
    if request.method == 'POST':
        forms = NewsForm(request.POST)
        if forms.is_valid():

            messages.success(request, f'News scrapped successfully!')
            return redirect('all_news')
    else:
        forms = NewsForm()
    context = {'forms': forms }
    return render(request, 'news/news_form.html',context)

class NewsFormView(View):
    form_class = NewsForm
    template_name = 'news/news_form.html'

def search(request):

    news_ = News.objects.order_by('?') # to get unordered/shuffled list

    if request.method == 'GET':
        query= request.GET.get('search')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(content__icontains=query) | Q(author__icontains=query)

            results= News.objects.filter(lookups).distinct()

            context={
                'results': results,
            }
            print(results)
            return render(request, 'news/search_result.html', context)

        else:
            return redirect('all-news')

    else:
        return redirect('all-news')

def all_news (request):
    queryset = News.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 3)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        "news":queryset
    }
    return render(request,'news/all_news.html',context)

class NewsListView(ListView):
    model = News
    template_name = 'news/all_news.html'  
    context_object_name = 'news'  
    paginate_by = 3
    queryset = News.objects.all() 


def filterByDate(request):

    news = News.objects.order_by('?')

    if request.method == 'GET':
        query= request.GET.get('filterByDate',False)
        print(query, '*******************')

        if query is not None:
            if query == 'today':
                today = datetime.datetime.today().strftime('%Y-%m-%d')
                news = News.objects.filter(date_published=today)
            elif query == 'latest':
                news = News.objects.order_by('-date_published')
            else:
                news = News.objects.order_by('date_published')
            page = request.GET.get('page', 1)
            paginator = Paginator(news, 3)
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


# def index(request):
#     user_list = User.objects.all()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(user_list, 10)
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)

#     return render(request, 'core/user_list.html', { 'users': users })