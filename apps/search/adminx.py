# -*- coding: utf-8 -*-
import xadmin
from search.models import JdBrand

__author__ = 'yvkang'
__date__ = '2019/2/14 0014 12:02'

class JdBrandAdmin(object):
    list_display = ['brand_id','brand_name']
    # 搜索
    search_fields = ['brand_id','brand_name']
    # 筛选
    list_filter = ['brand_id','brand_name']
    model_icon = 'fa fa-bars'
    # 导出文件
    list_export = ('xls', 'xml', 'json')
    # 刷新时间
    refresh_times = (5, 10)
    # 数据即时编辑
    list_editable = ['brand_name']
    # 排序
    ordering = ['brand_id']
    #分页
    list_per_page = 50

xadmin.site.register(JdBrand,JdBrandAdmin)