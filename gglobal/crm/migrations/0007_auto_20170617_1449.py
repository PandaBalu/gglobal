# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-17 11:49
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20170617_0247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_service',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_trouble',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='salary',
            name='state',
            field=django_fsm.FSMField(choices=[('waiting_paid', 'Ожидается оплата'), ('approved_paid', 'Проверяется оплата'), ('complete_paid', 'Оплачен')], default='wait_paid', max_length=50, protected=True, verbose_name='Статус'),
        ),
    ]
