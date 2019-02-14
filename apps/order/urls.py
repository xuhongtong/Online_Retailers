# -*- coding:utf-8 -*-
from order import views

__author__ = 'xht'
__date__ = '2019/1/24 19:52'

from django.conf.urls import url


urlpatterns = [
    url(r'', views.order, name='order'),
]
