# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20170707_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='./gallery/static/gallery/img'),
        ),
    ]
