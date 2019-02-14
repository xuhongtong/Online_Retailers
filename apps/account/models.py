from django.db import models


# Create your models here.
# from django.contrib.auth.models import AbstractUser


class User(models.Model):
    uid = models.AutoField(primary_key=True, verbose_name="用户ID")
    username = models.CharField(max_length=16, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.CharField(max_length=64, unique=True, verbose_name="邮箱地址")
    # phone = models.CharField(max_length=11,unique=True)
    active = models.BooleanField(default=0, verbose_name="活跃状态")
    is_delete = models.BooleanField(default=0, verbose_name="是否删除")

    # u_ticket=models.CharField(max_length=30,null=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name





# class JdBrand(models.Model):
#     brand_id=models.AutoField(primary_key=True)
#     title=


