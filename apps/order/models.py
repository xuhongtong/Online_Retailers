from django.db import models

# Create your models here.


class Order(models.Model):
    oid=models.AutoField(primary_key=True)
    order_code=models.IntegerField()
    uid=models.IntegerField()
    create_date=models.DateTimeField(auto_now_add=True)
    pay_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=1)

    class Meta:
        db_table='order'