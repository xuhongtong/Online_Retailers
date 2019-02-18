# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/1/17 17:29'

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Crawl(CrawlSpider):
    name = 'jd3'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    rules = (
        Rule(LinkExtractor(allow='www.jd.com'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        pass
