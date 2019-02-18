# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/1/17 17:29'

import scrapy


class Base(scrapy.Spider):
    name = 'jd12'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        pass
