# Generated by Django 3.0.6 on 2020-07-03 13:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PClub_contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=200)),
                ('contest_name', models.CharField(max_length=200)),
                ('contest_duration', models.CharField(max_length=100)),
                ('contest_start', models.DateTimeField(blank=True)),
                ('contest_end', models.DateTimeField(blank=True)),
                ('contest_link', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=200)),
                ('platform_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Server_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_update_time', models.DateTimeField(default=datetime.datetime(2020, 7, 3, 18, 53, 7, 839232))),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(max_length=200)),
                ('contest_duration', models.CharField(max_length=100)),
                ('contest_start', models.DateTimeField(blank=True)),
                ('contest_end', models.DateTimeField(blank=True)),
                ('contest_link', models.URLField()),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitive_programming.Platform')),
            ],
        ),
    ]