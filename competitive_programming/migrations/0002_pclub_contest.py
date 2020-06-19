# Generated by Django 3.0.6 on 2020-06-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitive_programming', '0001_initial'),
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
                ('contest_end', models.DateField(blank=True)),
                ('contest_link', models.URLField(max_length=100)),
            ],
        ),
    ]