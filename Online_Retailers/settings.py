import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 忽略apps目录的存在(注册app不用apps.account，直接用account其他导包也一样)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r8bvq*zfw%8bow(t*lbzlcyu(+!-@-7t)0sfcjk^_$%oy-%7%i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

# 注册系统app
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 注册第三方app
EXT_APPS = [
    'xadmin',
    'crispy_forms',
    'reversion',
    'captcha'
]

# 注册自定义app
CUSTOM_APPS = [
    'account',
    'main',
    'search',
    'shop',
    'shopcart',
    'comment',
    'order'
    'pay',
]

# 拼接apps
INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Online_Retailers.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.shopcart.context_processors.count',
            ],
        },
    },
]

WSGI_APPLICATION = 'Online_Retailers.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online_retailers',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'online_retailers',
#         'USER': 'tom',
#         'PASSWORD': '123456',
#         'HOST': '192.168.50.7',
#         'PORT': '3306',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online_retailers',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# 静态文件目录配置
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# ===============发送邮箱配置==========
# 发送邮件的服务器地址
EMAIL_HOST = 'smtp.163.com'
# 发送邮件端口
EMAIL_PORT = 25
# 发送邮件默认的名称
EMAIL_HOST_USER = 'yinyaowhy@163.com'
# 授权码
EMAIL_HOST_PASSWORD = 'python1805'
# 是否启用tls安全协议
EMAIL_USE_TLS = True

# 是否启用SSL安全协议
# EMAIL_USE_SSL = True
# 发送超时时间
# EMAIL_TIMEOUT =
# 默认邮件


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ===============发送邮箱配置 end ==========


# 验证码
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'



# ======================== start 支付模块 ============================
# 注册应用时支付宝生成的app_id
APP_ID = '2016092200574031'
# 支付网关
ALI_PAY_URL = 'https://openapi.alipaydev.com/gateway.do'
# 设置自己的私钥
APP_PRIVATE_STRING  = open(BASE_DIR + '/key/app_private_key.pem').read()
# 将自己的公钥放在支付宝上
ALIPAY_PUBLIC_KEY_STRING = open(BASE_DIR + '/key/app_public_key.pem').read()
# ==========================end 支付宝相关配置 ================







