# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-17 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orderdetail_create_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='create_time',
        ),
        migrations.AddField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]