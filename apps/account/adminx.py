# -*- coding: utf-8 -*-
import xadmin
from account.models import User

__author__ = 'yvkang'
__date__ = '2019/2/14 0014 11:48'


# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True
#
# class GlobalSettings(object):
#     site_title = "商城后台管理系统"
#     site_footer = "网上商城"
#     menu_style = 'accordion'

class UsersAdmin(object):
    list_display = ['uid','username','password','email','active','is_delete']
    # 搜索
    search_fields = ['uid','username','password','email','active','is_delete']
    # 筛选
    list_filter = ['username','password','email','active','is_delete']
    model_icon = 'fa fa-user'
    # 导出文件
    list_export = ('xls', 'xml', 'json')
    # 刷新时间
    refresh_times = (5, 10)
    # 数据即时编辑
    list_editable = ['username','password','email','active','is_delete']
    # 排序
    ordering = ['uid']
    #分页
    list_per_page = 50

xadmin.site.register(User,UsersAdmin)