# Generated by Django 2.1.4 on 2018-12-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20181215_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackmanager',
            name='default_cnvs',
            field=models.BooleanField(default=True),
        ),
    ]