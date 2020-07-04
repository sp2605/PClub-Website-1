# Generated by Django 3.0.6 on 2020-07-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_description', models.TextField()),
                ('faculty_advisor_fn', models.CharField(max_length=30)),
                ('faculty_advisor_ln', models.CharField(max_length=30)),
                ('faculty_advisor_photo', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('secretary_fn', models.CharField(max_length=30)),
                ('secretary_ln', models.CharField(max_length=30)),
                ('secretary_photo', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('joint_secretary_fn', models.CharField(max_length=30)),
                ('joint_secretary_ln', models.CharField(max_length=30)),
                ('joint_secretary_photo', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('treasurer_fn', models.CharField(max_length=30)),
                ('treasurer_ln', models.CharField(max_length=30)),
                ('treasurer_photo', models.ImageField(blank=True, default=None, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_fn', models.CharField(max_length=30)),
                ('member_ln', models.CharField(max_length=30)),
            ],
        ),
    ]