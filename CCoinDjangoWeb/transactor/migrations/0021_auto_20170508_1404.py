# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactor', '0020_auto_20170508_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsonrpcserverinfo',
            name='controlAdminAccount',
            field=models.CharField(default='test', max_length=120),
        ),
        migrations.AddField(
            model_name='jsonrpcserverinfo',
            name='controlAdminPassword',
            field=models.CharField(default='test', max_length=120),
        ),
    ]
