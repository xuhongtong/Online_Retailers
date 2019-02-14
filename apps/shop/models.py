from django.db import models

# Create your models here.
from main.models import JdThirdCate
from search.models import JdBrand


class JdShop(models.Model):
    id = models.AutoField(primary_key=True,verbose_name = '商品ID')
    title = models.CharField(max_length=80,verbose_name = '商品名称')
    original_price = models.IntegerField(verbose_name = '商品原价')
    promote_price = models.IntegerField(verbose_name = '商品促销价')
    img_url = models.CharField(max_length=256,verbose_name = '商品图片地址')
    month_sales = models.IntegerField(verbose_name = '商品月销量')
    total_sales = models.IntegerField(verbose_name = '商品总销量')
    stock=models.IntegerField(verbose_name = '商品点击量')
    total_evaluates = models.IntegerField(verbose_name = '商品评论数')
    third_cate_id = models.ForeignKey(to=JdThirdCate, on_delete=models.CASCADE, db_column='third_cate_id')
    brand_name=models.CharField(max_length=64,default='',verbose_name = '商品品牌')

    class Meta:
        db_table = 'jd_shop'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
