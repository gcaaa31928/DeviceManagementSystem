# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-18 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceManagementSystemApp', '0002_students_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devices',
            old_name='date_time',
            new_name='check_in_date_time',
        ),
        migrations.AddField(
            model_name='devices',
            name='token',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]