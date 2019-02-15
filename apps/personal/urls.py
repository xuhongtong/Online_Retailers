
from django.contrib import admin
from django.conf.urls import url, include
from personal import views

urlpatterns = [
    url(r'^personal/', views.personal_view, name='personal'),
    url(r'^information/',views.information_view,name='information'),
    url(r'^address/',views.address_view,name='address'),
    url(r'^bill/',views.bill_view,name='bill'),
    url(r'^order_manage/',views.order_manage,name='order_manage'),
    url(r'^orderinfo/',views.orderinfo_view,name='orderinfo'),

]

