# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceManagementSystemApp', '0005_auto_20160823_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='check_in_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='issues',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='DeviceManagementSystemApp.Students'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='used_for',
            field=models.TextField(null=True),
        ),
    ]
