# Generated by Django 2.2.24 on 2021-07-03 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latlong', models.CharField(max_length=20)),
                ('initials', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Postcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateField()),
                ('received', models.DateField()),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postcards.Country')),
            ],
        ),
    ]
