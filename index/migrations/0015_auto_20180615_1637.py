# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_modify'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Modify',
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
