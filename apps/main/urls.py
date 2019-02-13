# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/1/24 19:42'


from django.conf.urls import url
from main import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
]