from django.db import models
# Create your models here.
from main.models import JdThirdCate
class JdBrand(models.Model):
    brand_id = models.AutoField(primary_key=True,verbose_name='商品品牌ID')
    brand_name = models.CharField(max_length=64,verbose_name='商品品牌名称')
    third_cate_id = models.ForeignKey(to=JdThirdCate, on_delete=models.CASCADE, db_column='third_cate_id')
    class Meta:
        db_table = 'jd_brand'
        verbose_name = '商品品牌'
        verbose_name_plural = verbose_name


