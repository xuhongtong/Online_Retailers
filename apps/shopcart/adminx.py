# -*- coding: utf-8 -*-
import xadmin
from shopcart.models import ShopCart

__author__ = 'yvkang'
__date__ = '2019/2/14 0014 12:03'


class ShopcartAdmin(object):
    list_display = ['cart_id','number','uid','shop_id']
    search_fields = ['cart_id','number','uid','shop_id']
    list_filter = ['cart_id','number','uid','shop_id']
    model_icon = 'fa fa-bars'
    list_export = ('xls', 'xml', 'json')
    refresh_times = (5, 10)
    list_editable = ['number','uid','shop_id']
    ordering = ['cart_id']
    list_per_page = 20

xadmin.site.register(ShopCart,ShopcartAdmin)