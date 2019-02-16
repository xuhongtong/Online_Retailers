# -*- coding: utf-8 -*-
__author__ = 'yvkang'
__date__ = '2019/2/14 0014 11:55'
import xadmin
from shop.models import JdShop

class ShopAdmin(object):
    list_display = ['id','title','original_price','promote_price','img_url','month_sales','total_sales','stock',
                    'total_evaluates','brand_name']
    # 搜索
    search_fields = ['id','title','original_price','promote_price','img_url','month_sales','total_sales','stock',
                     'total_evaluates','brand_name']
    # 筛选
    list_filter = ['id','title','original_price','promote_price','img_url','month_sales','total_sales','stock',
                   'total_evaluates','brand_name']
    model_icon = 'fa fa-archive'
    # 导出文件
    list_export = ('xls', 'xml', 'json')
    # 刷新时间
    refresh_times = (5, 10)
    # 数据即时编辑
    list_editable = ['title','original_price','promote_price','img_url','month_sales','total_sales','stock',
                     'total_evaluates','brand_name']
    # 排序
    ordering = ['id']
    # 分页
    list_per_page = 10

xadmin.site.register(JdShop,ShopAdmin)