# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_searchlog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchlog',
            name='number_of_results',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]