# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/1/24 19:52'

from django.conf.urls import url
from search_key import views

urlpatterns = [
    url(r'', views.search, name='searching'),
    # 分类路由
]
