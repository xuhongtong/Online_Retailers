from django.db import models

# Create your models here.
# from account.models import User
# from shop.models import JdShop


class ShopCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    uid = models.IntegerField()
    shop_id = models.IntegerField()
    is_valid = models.BooleanField(default=1)
    is_delete = models.BooleanField(default=1)

    class Meta:
        db_table = 'Jd_ShopCart'
