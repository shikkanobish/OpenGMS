# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-25 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20171125_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_flag',
            field=models.IntegerField(default=1),
        ),
    ]