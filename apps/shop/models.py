from django.db import models

# Create your models here.
from main.models import JdThirdCate
from search.models import JdBrand


class JdShop(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    original_price = models.IntegerField()
    promote_price = models.IntegerField()
    img_url = models.CharField(max_length=256)
    month_sales = models.IntegerField()
    total_sales = models.IntegerField()
    total_evaluates = models.IntegerField()
    third_cate_id = models.ForeignKey(to=JdThirdCate, on_delete=models.CASCADE, db_column='third_cate_id')
    # brand_name = models.ForeignKey(to=JdBrand, on_delete=models.CASCADE, db_column='brand_name')
    brand_name=models.CharField(max_length=64)

    class Meta:
        db_table = 'jd_shop'
