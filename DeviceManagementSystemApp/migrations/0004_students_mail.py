# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceManagementSystemApp', '0003_auto_20160818_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
