# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactor', '0018_auto_20170508_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsonrpcserverinfo',
            name='controlAdminAccount',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='jsonrpcserverinfo',
            name='controlAdminPassword',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
