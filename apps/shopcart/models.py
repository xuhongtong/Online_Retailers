from django.db import models

# Create your models here.
# from account.models import User
# from shop.models import JdShop
from account.models import User
from shop.models import JdShop


class ShopCart(models.Model):
    cart_id = models.AutoField(primary_key=True,verbose_name='购物车ID')
    number = models.IntegerField(verbose_name='购物数量')
    uid = models.IntegerField(verbose_name='用户ID')
    # uid = models.ForeignKey(to=User, on_delete=models.CASCADE, db_column='uid')
    shop_id = models.IntegerField(verbose_name='商品ID')
    # shop_id = models.ForeignKey(to=JdShop, on_delete=models.CASCADE, db_column='shop_id')
    # 1为未勾选，0为勾选，默认未勾选
    is_valid = models.BooleanField(default=1)
    # 0为删除，1为未删除，默认未删除
    is_delete = models.BooleanField(default=1)
    class Meta:
        db_table = 'Jd_ShopCart'
        verbose_name = '购物车信息'
        verbose_name_plural = verbose_name

