# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-08 01:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_auto_20161005_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=300)),
                ('City', models.CharField(max_length=300)),
                ('Name', models.CharField(max_length=300)),
                ('Address', models.CharField(max_length=300)),
                ('CompanyName', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='f_lat',
            field=models.CharField(default=datetime.datetime(2016, 10, 8, 1, 12, 55, 843587, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='f_long',
            field=models.CharField(default=datetime.datetime(2016, 10, 8, 1, 13, 16, 134945, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
