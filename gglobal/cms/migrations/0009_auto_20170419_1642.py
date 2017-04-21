# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-19 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_mastercrmprofile_avatar'),
        ('cms', '0008_masters_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, null=True)),
                ('master', models.ManyToManyField(blank=True, null=True, to='users.MasterCRMProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='masters',
            name='master',
        ),
        migrations.DeleteModel(
            name='Masters',
        ),
    ]
