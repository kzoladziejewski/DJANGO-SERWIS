# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-01 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180501_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='Number_Of_Answer',
            field=models.IntegerField(default=0),
        ),
    ]
