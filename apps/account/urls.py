# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/1/15 15:54'


from django.conf.urls import url
from account import views
urlpatterns = [
    url('register/', views.register, name='register'),
    url('login/', views.login_view, name='login'),
    url('logout/', views.logout_view, name='logout'),
    # url('mail/', views.hello_mail),
    url('active/', views.active_account),
    url('ref/', views.refresh_code,name='ref'),
]