# Generated by Django 3.0.6 on 2020-06-24 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_announce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='announcement_image',
        ),
    ]