# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactor', '0003_auto_20170414_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonRPCServerInfo',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=120)),
                ('port', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=120),
        ),
    ]
