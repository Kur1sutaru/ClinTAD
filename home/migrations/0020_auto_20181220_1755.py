# Generated by Django 2.1.4 on 2018-12-21 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20181220_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hpo',
            name='comment',
            field=models.CharField(default='', max_length=1200),
        ),
        migrations.AlterField(
            model_name='hpo',
            name='definition',
            field=models.CharField(default='', max_length=1200),
        ),
    ]