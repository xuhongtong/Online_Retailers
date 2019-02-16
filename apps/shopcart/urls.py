# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/1/24 19:42'


from django.conf.urls import url
from apps.shopcart import views


urlpatterns = [
    url(r'^$',views.add_cart,name='add_cart'),
    url(r'shopcart',views.shopcart,name='shopcart'),
    url(r'update_cart',views.update_cart,name='update_cart'),
]