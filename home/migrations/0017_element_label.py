# Generated by Django 2.1.4 on 2018-12-20 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20181218_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='label',
            field=models.CharField(default='', max_length=200),
        ),
    ]