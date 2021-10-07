from django.urls import path, include
from . import views 
# from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('newsForm', views.news_scrape, name='news-form'),
    path('nsearch',views.search, name ='nsearch'),
    path('allNews',views.all_news, name ='all-news'),
    path('filterByDate',views.filter_by_date, name ='filter-by-date'),
    path('<slug:slug>', views.news_detail, name="news-detail"),
]