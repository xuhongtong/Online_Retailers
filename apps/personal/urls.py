
from django.contrib import admin
from django.conf.urls import url, include
from personal import views

urlpatterns = [
    # 个人中心主页
    url(r'^personal/', views.personal_view, name='personal'),
    # 个人中心个人信息页
    url(r'^information/',views.information_view,name='information'),
    # 安全设置
    url(r'^safety/',views.safety_view,name='safety'),
    # 地址管理
    url(r'^address/',views.address_view,name='address'),

    url(r'^bill/',views.bill_view,name='bill'),
    url(r'^order_manage/',views.order_manage,name='order_manage'),
    url(r'^orderinfo/',views.orderinfo_view,name='orderinfo'),


]

