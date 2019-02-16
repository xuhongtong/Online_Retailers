from django.db import models

from django.contrib.auth.models import AbstractUser


class User(models.Model):
    uid = models.AutoField(primary_key=True, verbose_name="用户ID")
<<<<<<< HEAD
    username = models.CharField(max_length=16, unique=True, verbose_name="用户名")
    phone=models.IntegerField(default=123)
=======
    name = models.CharField(max_length=255,null=True,verbose_name='用户姓名')
    sex = models.CharField(max_length=11,choices=(('male','男'),('female','女'),('secret','保密')),null=False,verbose_name='性别')
    birthday = models.CharField(max_length=255,verbose_name='生日',default='1970-10-10')
    nickname = models.CharField(max_length=16, unique=True, verbose_name="用户昵称")
>>>>>>> origin/develop
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.CharField(max_length=64, unique=True, verbose_name="邮箱地址")
    phone = models.IntegerField(unique=True,null=True)
    active = models.BooleanField(default=0, verbose_name="活跃状态")
    is_delete = models.BooleanField(default=0, verbose_name="是否删除")
    safety_score = models.IntegerField(verbose_name='账户安全评分',default=0)

    # u_ticket=models.CharField(max_length=30,null=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address(models.Model):
    address_id=models.AutoField(primary_key=True)
    detail=models.CharField(max_length=256)
    uid=models.ForeignKey(to=User,on_delete=models.CASCADE, db_column='uid')

    class Meta:
        db_table='address'

