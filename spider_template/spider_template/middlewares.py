# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging
import random
import time

from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.http import HtmlResponse
from selenium.webdriver import ActionChains

from settings import IP_PROXY_LIST, USER_AGENT_LIST


class SpiderTemplateSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SpiderTemplateDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        # return response
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class IPProxyMiddleWare(object):
    '''
    ip 代理池
    '''

    def process_request(self, request, spider):
        # 从list中选取IP，设置到request
        ip_proxy = random.choice(IP_PROXY_LIST)
        if ip_proxy:
            request.meta['proxies'] = ip_proxy  # 此处关键字proxies不能错
            print(f"IP_PROXY:{ip_proxy}")

    def process_exception(self, request, exception, spider):
        error_info = f"spider:{spider.name} MyIPProxyMiddleWare has error with {exception}"
        print(error_info)
        logging.error(error_info)


class RotateUserAgentMiddleware(UserAgentMiddleware):
    '''
    用户代理中间件（处于下载中间件位置）
    UA代理池属于下载中间件，在下载中间件中的process_request的时候往request请求头部加入User-Agent
    从列表中随机选取一个ua
    '''

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
            print(f"User-Agent:{user_agent} is using.")
        return None

    def process_exception(self, request, exception, spider):
        error_info = f"spider:{spider.name} RotateUserAgentMiddleware has error with {exception}"
        print(error_info)
        logging.error(error_info)


class SeleniumDownloaderMiddleWare(object):
    def process_request(self, request, spider):
        actions = ActionChains(spider.driver)
        if spider.name == 'jd1' and request.meta.get('type') == 'home':
            spider.driver.get(request.url)
            time.sleep(5)
            first_cates = spider.driver.find_elements_by_xpath("//div[@id='J_cate']/ul/li")
            try:
                count = 0
                for first_cate in first_cates:
                    spider.driver.execute_script("arguments[0].scrollIntoView();", first_cate)
                    time.sleep(1)
                    if count == 0:
                        actions.move_to_element(first_cate).perform()
                    count = 1
            except Exception as e:
                print(f"############  there has error with {e} #### ")
            finally:
                with open("cate.html", "w", encoding="utf-8") as f:
                    f.write(spider.driver.page_source)
                return HtmlResponse(
                    url=spider.driver.current_url,
                    body=spider.driver.page_source,
                    request=request,
                    encoding="utf-8",
                )

        if spider.name == 'jd' and request.meta.get('type') == 'cate':
            spider.driver.get(request.url)
            time.sleep(5)
            js = "window.scrollTo(0, 20000)"
            spider.driver.execute_script(js)  # 往下翻滚页面
            time.sleep(5)
            print(f'+++++++++++++++++=,{spider.driver.current_url}')
            with open('test.html', 'w', encoding='utf8') as f:
                f.write(spider.driver.page_source)
            return HtmlResponse(
                url=spider.driver.current_url,
                body=spider.driver.page_source,
                request=request,
                encoding="utf-8",
            )

        if spider.name == 'jd' and request.meta.get('type') == 'detail':
            spider.driver.get(request.url)
            time.sleep(5)
            return HtmlResponse(
                url=spider.driver.current_url,
                body=spider.driver.page_source,
                request=request,
                encoding="utf-8",
                # meta=request.meta
            )
