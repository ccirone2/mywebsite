# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 16:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20170707_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='date_built',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 7, 16, 54, 7, 842000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='date_uploaded',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 7, 7, 16, 54, 51, 31000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
