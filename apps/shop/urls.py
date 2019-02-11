# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/2/4 21:31'

from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'detail', views.shop, name='detail'),
]
