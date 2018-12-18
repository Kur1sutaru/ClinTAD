# Generated by Django 2.1.4 on 2018-12-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_variant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='end',
            new_name='inner_end',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='start',
            new_name='inner_start',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='gains',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='losses',
        ),
        migrations.AddField(
            model_name='variant',
            name='frequency',
            field=models.FloatField(default=-1),
        ),
        migrations.AddField(
            model_name='variant',
            name='outer_end',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='variant',
            name='outer_start',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='variant',
            name='subtype',
            field=models.CharField(default='', max_length=5),
        ),
    ]