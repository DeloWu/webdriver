# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from django.conf.urls import url


app_name = 'webdriver'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^translator/$', views.translator, name='translator'),
	url(r'^apiTest/$', views.apiTest, name='apiTest'),
	url(r'^webUrls/$', views.webUrls, name='webUrls'),
	url(r'^timestamps/$', views.timestamps, name='timestamps'),
	url(r'^jsonFormat/$', views.jsonFormat, name='jsonFormat'),
	url(r'^createData/$', views.createData, name='createData'),
	url(r'^svnSpace/(\d{1,2})/$', views.svnSpace, name='svnSpace'),
	url(r'^upload/(\d{1,2})/$', views.upload, name='upload'),
	url(r'^download/$', views.download_file, name='download'),
	url(r'^searchFile/$', views.searchFile, name='searchFile'),
]