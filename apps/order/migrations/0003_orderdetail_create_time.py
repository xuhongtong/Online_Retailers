# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-17 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190217_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]