
from django.conf.urls import url, include
from django.contrib import admin
from article import views
import django.conf.urls.static
admin.autodiscover()

urlpatterns = [
    django.conf.urls.url(r'^1/', views.basic_one, name='basic_one'),
    django.conf.urls.url(r'^2/', views.template_two, name='template_two'),
    django.conf.urls.url(r'^3/', views.template_three, name='template_three'),
    django.conf.urls.url(r'^articles/all/$', views.articles, name='articles'),
    django.conf.urls.url(r'^articles/get/(?P<article_id>\d+)/$', views.article, name='article'),
    django.conf.urls.url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike, name='addlike'),
    django.conf.urls.url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment, name='addcomment'),
    django.conf.urls.url(r'^$', views.articles, name='articles')
]