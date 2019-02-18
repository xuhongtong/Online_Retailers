# -*- coding: utf-8 -*-
import hashlib

import scrapy
from scrapy import Request
import re
from items import JdFirstCateItem, JdSecondCateItem, JdThirdCateItem
from utils.bshead import create_bs_driver

# p = re.compile(r"<body>.*</body>")


def create_fingerprint2(url, type='md5'):
    minst = hashlib.md5() if type == 'md5' else hashlib.sha1()
    minst.update(url.encode('utf8'))
    return minst.hexdigest()


class Jd1Spider(scrapy.Spider):
    name = 'jd1'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def __init__(self):
        scrapy.Spider.__init__(self, self.name)
        self.driver = create_bs_driver()
        self.driver.set_page_load_timeout(20)

    def __del__(self):
        self.driver.quit()

    def start_requests(self):
        for url in self.start_urls:
            r = Request(url=url, dont_filter=True, meta={'type': 'home'})
            yield r

    def parse(self, response):
        print(response)
        first_cates = response.xpath("//div[@id='J_cate']/ul/li")

        # sub_cates = response.xpath('//div[@id="J_popCtn"]/div/div[@class="cate_part_col1"]/div[@class="cate_channel"]/a//text()').getall()
        # type = response.xpath('//div[@id="J_popCtn"]/div/div[@class="cate_part_col1"]/div[@class="cate_detail"]/dl/dd/a//text()').getall()

        counter = 1
        num1 = 1
        num2 = 1
        for cate in first_cates:
            # cate=cate.xpath("a//text()").extract()
            first_cate_id = counter
            first_cate_name = "/".join(cate.xpath("a//text()").extract())
            # print(cate)
            # print("1：\n",first_cate_name)
            item1 = JdFirstCateItem(first_cate_id=first_cate_id, first_cate_name=first_cate_name)
            print(item1)
            yield item1
            dls = response.xpath(f'//div[@id="cate_item{counter}"]/div[1]/div[2]/dl')
            # yield
            for dl in dls:
                second_cate_list = dl.xpath("dt/a/text()").extract()
                for second_cate in second_cate_list:
                    print(second_cate)
                    second_cate_id = num1
                    item2 = JdSecondCateItem(second_cate_id=second_cate_id, second_cate_name=second_cate,
                                             first_cate_id=first_cate_id)
                    print(item2)
                    yield item2
                    num1 += 1
                    # print("2：\n",sub_cate)
                    third_cate_list = dl.xpath("dd/a//text()").extract()
                    for third_cate in third_cate_list:
                        print(third_cate)
                        third_cate_id = num2
                        third_url = third_cate_id
                        item3 = JdThirdCateItem(third_cate_id=third_cate_id, third_cate_name=third_cate,
                                                second_cate_id=second_cate_id)
                        print(item3)
                        yield item3
                        num2 += 1
                        # yield scrapy.Request(url="",meta={"third_cate_id":third_cate_id},callback=self.pas)

                # print("3：\n",type)
            counter += 1
        print("end", counter)

        # second_cates=response.xpath('//div[@id="cate_item2"]/div[1]/div[2]/dl')
        # for j in second_cates:
        #
        #
        #
        #     second_cate=j.xpath('dt/a/text()').extract_first()
        #     item2=JdSecondCateItem(second_cate=second_cate)
        #     print('++++++++')
        #     print(item2)
        #     print('++++++++')
        #     yield item2
        # print('++++++++')
        # print(item1)
        # print('+++++')
        # yield item1

# 动态爬进中间件
