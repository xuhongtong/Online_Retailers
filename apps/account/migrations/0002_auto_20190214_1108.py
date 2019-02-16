# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-14 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=0, verbose_name='活跃状态'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=64, unique=True, verbose_name='邮箱地址'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=16, unique=True, verbose_name='用户名'),
        ),
    ]