from django.db import models

# Create your models here.


class Order(models.Model):
    oid=models.AutoField(primary_key=True)
    order_code=models.CharField(max_length=128)
    uid=models.IntegerField()
    total_money=models.DecimalField(max_digits = 7,decimal_places = 2,default=0 )
    # # create_date=models.DateTimeField(auto_now_add=True)
    # # pay_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=1)

    class Meta:
        db_table='order'


# class OrderDetail(models.Model):
#     id=models.AutoField(primary_key=True)
#     oid=models.IntegerField()
#     shop_id=models.IntegerField()
#     shop_name=models.CharField(max_length=64)
#     price=models.DecimalField(max_digits = 7,decimal_places = 2)
#     count=models.IntegerField()
