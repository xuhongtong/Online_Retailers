"""Online_Retailers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from account import views
from main import views
import xadmin
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    # url('admin/', admin.site.urls),
    url(r'^xadmin/',include(xadmin.site.urls)),
    url(r'^account/',include('account.urls')),
    url(r'',include('main.urls')),
    # url(r'^search_view',include('search.urls')),
    url(r'^search_view',include('search_key.urls')),
    url(r'^catelog',include('search.urls')),
    # url(r'^search',include('haystack.urls')), # 全文检索框架搜索引擎url
    url(r'^shop/',include('shop.urls')),
    url(r'^shopcart/',include('shopcart.urls')),
    url(r'^order/',include('order.urls')),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^person/',include('personal.urls')),
    url(r'^pay/',include('pay.urls')),

]
