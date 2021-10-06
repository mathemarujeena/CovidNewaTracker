from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('newsForm', views.index, name='news-form'),
    path('nsearch',views.search, name ='nsearch'),
    path('allNews',views.NewsListView.as_view(), name ='all-news'),
    path('filterByDate',views.filterByDate, name ='filter-by-date'),
]