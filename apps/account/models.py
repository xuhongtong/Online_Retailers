from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
# from django.contrib.auth.models import AbstractUser
from Online_Retailers import settings
# class UserProfile(AbstractUser):
#     """
#     用户
#     """
#     # nickname = models.CharField(max_length=30, null=True, blank=True, verbose_name='昵称')
#     name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
#     gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female", verbose_name="性别")
#     birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
#     payment = models.CharField(max_length=50, null=True, blank=True, verbose_name="支付密码")
#     mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
#     member = models.CharField(max_length=6, choices=((1,"普通用户"), (2, "VIP会员"), (3, "超级会员")), default=1, verbose_name="会员等级")
#     class Meta:
#         verbose_name = "管理员"
#         verbose_name_plural = verbose_name
#         db_table = 'auth_user'

class User(models.Model):
    uid = models.AutoField(primary_key=True, verbose_name="用户ID")
    name = models.CharField(max_length=255,null=True,verbose_name='用户姓名')
    nickname = models.CharField(max_length=16, unique=True, verbose_name="用户昵称")
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.CharField(max_length=64, unique=True, verbose_name="邮箱地址")
    phone = models.CharField(max_length=11,unique=True)
    active = models.BooleanField(default=0, verbose_name="活跃状态")
    is_delete = models.BooleanField(default=0, verbose_name="是否删除")

    # u_ticket=models.CharField(max_length=30,null=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name




