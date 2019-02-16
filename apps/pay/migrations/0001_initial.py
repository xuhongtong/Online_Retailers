# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-15 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_auto_20190214_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUser',
            fields=[
                ('oid', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('total_price', models.IntegerField(default=0)),
                ('status', models.IntegerField(verbose_name=((0, '未支付'), (1, '已支付'), (2, '已撤销')))),
                ('pay_time', models.DateTimeField(auto_now_add=True)),
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
            options={
                'db_table': 'order_user',
            },
        ),
    ]