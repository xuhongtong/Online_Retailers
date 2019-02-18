# -*- coding: utf-8 -*-

# Scrapy settings for spider_template project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider_template'

SPIDER_MODULES = ['spider_template.spiders']
NEWSPIDER_MODULE = 'spider_template.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'spider_template (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 是否遵守robots协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载延迟
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16


#对单个网站进行并发请求的最大值
# CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'spider_template.middlewares.SpiderTemplateSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'spider_template.middlewares.SpiderTemplateDownloaderMiddleware': 543,
    # UA中间件继承的父类
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    # UA代理池
    # 'spider_template.middlewares.RotateUserAgentMiddleware': 200,
    # IP代理池
    # 'spider_template.middlewares.IPProxyMiddleWare':300,
    # 动态爬取
    'spider_template.middlewares.SeleniumDownloaderMiddleWare':100,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 注册图片下载管道
    'spider_template.image_pipelines.MyImagesPipeline': 300,
    # 注册mysql存储同步通道
    'spider_template.sync_mysql_pipelines.JdPipeline': 200,
    # 注册Mongo存储通道
    # 'spider_template.mongo_pipelines.mongo_pipelines': 150,
    # 注册分布式爬虫
    # 'scrapy_redis.pipelines.RedisPipeline': 350,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# mysql连接配置
DB_SET_MAP = {
    'user': 'root',
    'passwd': '123456',
    'host': '127.0.0.1',
    'port': '3306',
    'db': 'online_test',
}

# Mongo连接配置
MONGODB_SETTINGS = {
    'db_host': '127.0.0.1',
    'db_name': 'spider_test',
    'db_port': 27017,
    'collect_sy': 'sy',
}

# 配置图片下载相关配置
IMAGES_STORE = 'images'
IMAGES_THUMBS = {
    'small':(50,20),
    'big': (250, 250),
}

# ######## 配置日志 ############
LOG_LEVEL = "INFO"

from datetime import datetime
import os

today = datetime.now()

LOG_DIR = "log"
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

LOG_FILE = "{}/scrapy_{}_{}_{}.log".format(LOG_DIR, today.year, today.month, today.day)

#################################

# UA代理池  (1)手动写  （2）fake_useragent第三方库
with open("proxy_pool/ua_list.txt", "r") as f:
    USER_AGENT_LIST = f.readlines()
USER_AGENT_LIST = [user_agent.strip() for user_agent in USER_AGENT_LIST]

# IP代理
with open("proxy_pool/proxy_list.txt", "r") as f:
    IP_PROXY_LIST = f.readlines()
IP_PROXY_LIST = [ip_agent.strip() for ip_agent in IP_PROXY_LIST]

# ###################分布式配置 ######################
# 调度器策略 --- scrapy_redis.scheduler.Scheduler
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
import platform

system = platform.system()

SYSTEM_PROCESS_MAP = {
    "Darwin": "scrapy_redis.bf_dupefilter.RFPDupeFilter",  # Mac
    "Linux": "scrapy_redis.bf_dupefilter.RFPDupeFilter",
    "Windows": "scrapy_redis.dupefilter.RFPDupeFilter",
}

# 去重策略 --- scrapy_redis.dupefilter.RFPDupeFilter （此去重器继承scrapy自带的去重器）
# DUPEFILTER_CLASS = "scrapy_redis.bf_dupefilter.RFPDupeFilter"
DUPEFILTER_CLASS = SYSTEM_PROCESS_MAP.get(system)

REDIS_MAP = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0,
}

# redis配置地址
REDIS_URL = f"redis://{REDIS_MAP['host']}:{REDIS_MAP['port']}"  # 等同于"redis://127.0.0.1:6379/0"

# 此开关表示，如果当前分布式爬取关闭后，是否保留原来调度器中去重记录，关系到是否重爬
SCHEDULER_PERSIST = True

DOWNLOAD_DELAY = 2

DEPLOY_ONLINE = 0  # 1 --- ONLINE, 0 --- test

# #################### 分布式配置 end ##########################
