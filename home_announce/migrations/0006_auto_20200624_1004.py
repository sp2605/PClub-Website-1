# Generated by Django 3.0.6 on 2020-06-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_announce', '0005_daily'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='answer',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]