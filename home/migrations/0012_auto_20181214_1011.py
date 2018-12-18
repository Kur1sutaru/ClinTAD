# Generated by Django 2.1.4 on 2018-12-14 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0011_auto_20181213_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='UT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='element',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='home.Track'),
        ),
        migrations.AlterField(
            model_name='track',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ut',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Track'),
        ),
        migrations.AddField(
            model_name='ut',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='ut',
            unique_together={('track', 'user')},
        ),
    ]