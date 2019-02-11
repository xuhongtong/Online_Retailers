from django.db import models


# Create your models here.
# from django.contrib.auth.models import AbstractUser


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64, unique=True)

    # u_ticket=models.CharField(max_length=30,null=True)

    class Meta:
        db_table = 'user'





# class JdBrand(models.Model):
#     brand_id=models.AutoField(primary_key=True)
#     title=


