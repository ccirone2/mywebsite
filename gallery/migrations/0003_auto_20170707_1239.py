# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20170707_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageTitle', models.CharField(max_length=120)),
                ('ImageSubTitle', models.CharField(blank=True, max_length=120, null=True)),
                ('ImageDesc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='GalleryImages',
        ),
    ]