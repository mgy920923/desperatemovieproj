# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-12 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_auto_20180412_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Director',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
    ]
