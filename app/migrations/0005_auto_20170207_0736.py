# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-07 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20161207_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterModelTable(
            name='artist',
            table='artist',
        ),
    ]
