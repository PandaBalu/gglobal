# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-02 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20170502_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcrmprofile',
            name='name',
            field=models.CharField(max_length=25, null=True, verbose_name='Имя'),
        ),
    ]
