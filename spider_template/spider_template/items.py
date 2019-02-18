# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderTemplateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# ##########定义京东item页面解析字典###################

# 一级分类
class JdFirstCateItem(scrapy.Item):
    first_cate_id = scrapy.Field()
    first_cate_name = scrapy.Field()

    # first_url=scrapy.Field()

    # 获取类名，用于管道查找对应item进行处理
    def get_name(self):
        return JdFirstCateItem.__name__


# 二级分类
class JdSecondCateItem(scrapy.Item):
    second_cate_id = scrapy.Field()
    second_cate_name = scrapy.Field()
    first_cate_id = scrapy.Field()

    # second_url = scrapy.Field()

    def get_name(self):
        return JdSecondCateItem.__name__


# 三级分类
class JdThirdCateItem(scrapy.Item):
    third_cate_id = scrapy.Field()
    third_cate_name = scrapy.Field()
    second_cate_id = scrapy.Field()

    # third_url = scrapy.Field()

    def get_name(self):
        return JdThirdCateItem.__name__


# 详情页
class JdDetailItem(scrapy.Item):
    # shop_id=scrapy.Field()
    title = scrapy.Field()
    # sub_title=scrapy.Field()
    # original_price=scrapy.Field()
    original_price = scrapy.Field()
    promote_price = scrapy.Field()
    img_url = scrapy.Field()
    stock = scrapy.Field()
    month_sales = scrapy.Field()
    total_sales = scrapy.Field()
    total_evaluates = scrapy.Field()
    third_cate_id = scrapy.Field()
    brand_name = scrapy.Field()

    # promote_price=scrapy.Field()
    # count=scrapy.Field()
    # create_date=scrapy.Field()

    def get_name(self):
        return JdDetailItem.__name__


# 分类页品牌表
class JdBrandItem(scrapy.Item):
    brand_name = scrapy.Field()
    third_cate_id = scrapy.Field()

    def get_name(self):
        return JdBrandItem.__name__

# 商品属性表
