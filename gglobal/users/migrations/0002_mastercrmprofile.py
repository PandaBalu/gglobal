# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 15:59
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.CITIES_CITY_MODEL),
        ('sites', '0003_set_site_domain_and_name'),
        migrations.swappable_dependency(settings.CITIES_COUNTRY_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterCRMProfile',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('raiting', models.IntegerField()),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.CITIES_CITY_MODEL)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.CITIES_COUNTRY_MODEL)),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
    ]