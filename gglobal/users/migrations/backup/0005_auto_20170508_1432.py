# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0028_auto_20170508_1432'),
        ('users', '0004_auto_20170507_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.ManyToManyField(to='crm.PhoneNumber', verbose_name='Номера телефонов'),
        ),
    ]