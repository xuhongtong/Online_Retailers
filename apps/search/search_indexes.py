# -*-coding: utf-8 -*-
__author__ = 'qqy'
__date__ = '2019/2/14 21:17'
from haystack import indexes
from search.models import JdBrand
class JdBrandIndex(indexes.SearchIndex,indexes.Indexable):
    # 创建一个text字段
    text=indexes.CharField(document=True,use_template=True)
    # 重载方法
    def get_model(self):
        return JdBrand
    def index_queryset(self, using=None):
        return self.get_model().objects.all()