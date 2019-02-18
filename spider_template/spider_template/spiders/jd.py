# -*- coding: utf-8 -*-
import random

import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from items import JdDetailItem, JdBrandItem
from utils.bshead import create_bs_driver


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    # 待爬取的品牌
    start_urls = ['https://list.jd.com/list.html?cat=9987,653,655'  # 鼠标
                  # 'https: // list.jd.com / list.html?cat = 670, 686, 689'  # 键盘
                  # 手机
                  ]

    def __init__(self):
        scrapy.Spider.__init__(self, self.name)
        self.driver = create_bs_driver()
        self.driver.set_page_load_timeout(60)

    def __del__(self):
        self.driver.quit()

    def start_requests(self):
        for url in self.start_urls:
            r = Request(url=url, dont_filter=True, callback=self.cate_parse, meta={'type': 'cate'})
            yield r

    # rules = (
    #     Rule(LinkExtractor(allow=r'item.jd.com/\d+'), callback='selenium_detail', follow=True),
    #     # Rule(LinkExtractor(allow=r'//item.jd.com/\d+.html'), callback='selenium_detail', follow=False),
    # )

    # def selenium_detail(self, response):
    #     url = response.url
    #     r = Request(url=url, dont_filter=True, callback=self.detail_parse, meta={"type": "detail"})
    #     yield r

    # 解析分类页面
    def cate_parse(self, response):
        detail_list = response.xpath('//div[@id="plist"]/ul/li')  # 爬取详情页
        brand_list = response.xpath('//ul[@id="brandsArea"]/li')  # 爬取分类页品牌

        # 遍历并解析品牌列表
        for brand in brand_list:
            brand_name = brand.xpath('a/@title').extract_first()
            third_cate_id = 95
            item = JdBrandItem(brand_name=brand_name, third_cate_id=third_cate_id)
            print(item)
            yield item

        # 遍历详情列表
        for detail in detail_list:
            url = 'http:' + detail.xpath('div/div[1]/a/@href').extract_first()
            r = Request(url=url, dont_filter=True, callback=self.detail_parse, meta={'type': 'detail'})
            yield r

    # 解析详情页面（商品信息部分）
    def detail_parse(self, response):
        title = response.xpath('//div[8]/div/div[2]/div[1]/text()').extract()
        title = ''.join(title).strip()
        original_price = response.xpath(
            '//div[8]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]/text()').extract_first()
        original_price = float(original_price)
        promote_price = original_price - 10
        img_url = 'http:' + response.xpath('//img[@id="spec-img"]/@src').extract_first()
        stock = random.randint(500, 1000)
        month_sales = random.randint(1000, 5000)
        total_sales = random.randint(10000, 50000)
        total_evaluates = random.randint(1, 1000)
        third_cate_id = 95
        brand_name=response.xpath('//div[@id="crumb-wrap"]/div/div[1]/div[7]/div/div/div[1]/a/text()').extract_first()
        item = JdDetailItem(title=title, original_price=original_price, promote_price=promote_price, img_url=img_url,
                            stock=stock, month_sales=month_sales, total_sales=total_sales,
                            total_evaluates=total_evaluates,third_cate_id=third_cate_id,brand_name=brand_name)
        print(item)
        yield item
