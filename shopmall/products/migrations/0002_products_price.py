# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-03 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]