# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-13 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180113_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='review_note',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='review_note',
            field=models.CharField(max_length=200, null=True),
        ),
    ]