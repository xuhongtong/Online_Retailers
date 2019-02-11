# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/1/24 19:52'

from django.conf.urls import url
from search import views

urlpatterns = [
    url(r'', views.search, name='search'),
]
