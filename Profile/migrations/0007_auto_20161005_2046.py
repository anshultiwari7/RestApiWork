# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='zipcode',
            field=models.CharField(max_length=20),
        ),
    ]
