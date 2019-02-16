# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-16 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('detail', models.CharField(max_length=256)),
                ('uid', models.IntegerField()),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='用户姓名')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女'), ('secret', '保密')], max_length=11, null=True, verbose_name='性别')),
                ('birthday', models.CharField(default='1970-10-10', max_length=255, verbose_name='生日')),
                ('nickname', models.CharField(max_length=16, null=True, unique=True, verbose_name='用户昵称')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='邮箱地址')),
                ('phone', models.IntegerField(null=True, unique=True)),
                ('active', models.BooleanField(default=0, verbose_name='活跃状态')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('safety_score', models.IntegerField(default=0, verbose_name='账户安全评分')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
        ),
    ]
