# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-25 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180925_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='hpo',
            name='comment',
            field=models.CharField(default='', max_length=500),
        ),
    ]
