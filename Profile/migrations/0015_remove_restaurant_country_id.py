# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-22 00:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0014_auto_20161022_0525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='country_id',
        ),
    ]
