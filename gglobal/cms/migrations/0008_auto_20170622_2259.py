# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_remove_basepage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityPageSnippetPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'Сниппет для страницы города',
                'verbose_name_plural': 'Сниппеты для страниц городов',
            },
        ),
        migrations.RemoveField(
            model_name='citypage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='citysnippetpage',
            name='city',
        ),
        migrations.AddField(
            model_name='citysnippetpage',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='citypagesnippetplacement',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_snippet_placements', to='cms.CityPage'),
        ),
        migrations.AddField(
            model_name='citypagesnippetplacement',
            name='snippet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cms.CitySnippetPage'),
        ),
    ]