from django.db import models

# Create your models here.
from account.models import User


class OrderUser(models.Model):
    oid = models.CharField(max_length=30,unique=True,primary_key=True)
    uid = models.ForeignKey(to=User,on_delete=models.CASCADE, db_column='uid')
    total_price = models.IntegerField(default=0,null=False)
    status = models.IntegerField(((0,'未支付'),(1,'已支付'),(2,'已撤销'),),)
    commit_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_user'
