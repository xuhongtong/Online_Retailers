# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-17 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('order_code', models.CharField(max_length=128)),
                ('uid', models.IntegerField()),
                ('total_money', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('status', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('oid', models.IntegerField()),
                ('shop_id', models.IntegerField()),
                ('shop_name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'order_detail',
            },
        ),
    ]
