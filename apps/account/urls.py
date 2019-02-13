# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/1/15 15:54'

from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'login/$',views.login_view,name='login'),
    url(r'register/$',views.register,name='register'),
    url(r'logout/$',views.logout,name='logout'),
]