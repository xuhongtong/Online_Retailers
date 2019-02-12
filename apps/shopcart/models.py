from django.db import models

# Create your models here.
# from account.models import User
# from shop.models import JdShop
from account.models import User
from shop.models import JdShop


class ShopCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    uid = models.IntegerField()
    # uid = models.ForeignKey(to=User, on_delete=models.CASCADE, db_column='uid')
    shop_id = models.IntegerField()
    # shop_id = models.ForeignKey(to=JdShop, on_delete=models.CASCADE, db_column='shop_id')
    is_valid = models.BooleanField(default=1)
    is_delete = models.BooleanField(default=1)

    class Meta:
        db_table = 'Jd_ShopCart'
