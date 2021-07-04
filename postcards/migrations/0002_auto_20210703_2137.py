# Generated by Django 2.2.24 on 2021-07-03 21:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='distance',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postcard',
            name='time_travel',
            field=models.CharField(default=django.utils.timezone.now, max_length=4),
            preserve_default=False,
        ),
    ]
