# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170518_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='city',
            field=models.CharField(blank=True, default='Windsor', max_length=100),
        ),
    ]
