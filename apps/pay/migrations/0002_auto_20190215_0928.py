# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-15 09:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderuser',
            old_name='pay_time',
            new_name='commit_time',
        ),
    ]
