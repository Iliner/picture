# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20180614_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, height_field='photo_height', null=True, upload_to='', width_field='photo_width'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_height',
            field=models.IntegerField(verbose_name=200),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_width',
            field=models.IntegerField(verbose_name=500),
        ),
    ]
