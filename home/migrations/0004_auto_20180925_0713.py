# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-25 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180925_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chromosome',
            name='number',
            field=models.CharField(default='', max_length=1),
        ),
    ]