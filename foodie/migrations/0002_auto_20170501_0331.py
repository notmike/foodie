# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='rating',
            field=models.FloatField(default=None),
        ),
    ]