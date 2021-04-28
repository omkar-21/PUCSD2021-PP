from django.urls import include, path
from news import views


NEWS_LIST = views.NewsViewSet.as_view({
    'post' : 'add_news',
    'get'  : 'list_all_news'
})
LATEST_NEWS = views.NewsViewSet.as_view({
    'get'  : 'latest_news'
})

urlpatterns = [
    path(r'list/', views.NewsViewSet.as_view(
        {'get': 'list_all_news'},name='news_list'
    )),
    path(r'add/', views.NewsViewSet.as_view(
        {'post': 'add_news'},name='news_added'
    )),    
    path(r'latest/', views.NewsViewSet.as_view(
        {'get': 'latest_news'},name='news_latest'
    )), 
]   