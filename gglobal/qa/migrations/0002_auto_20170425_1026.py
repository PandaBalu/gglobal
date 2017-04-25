# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-25 07:26
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0003_set_site_domain_and_name'),
        ('users', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQAProfile',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('points', models.IntegerField(default=0)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='taggedwhatever',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa_taggedwhatever_tagged_items', to='contenttypes.ContentType', verbose_name='Content type'),
        ),
        migrations.AddField(
            model_name='taggedwhatever',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa_taggedwhatever_items', to='qa.MyCustomTag'),
        ),
        migrations.AddField(
            model_name='questionvote',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Question'),
        ),
        migrations.AddField(
            model_name='questionvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Question'),
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='qa.TaggedWhatever', to='qa.MyCustomTag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answervote',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Answer'),
        ),
        migrations.AddField(
            model_name='answervote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Answer'),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='questionvote',
            unique_together=set([('user', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='answervote',
            unique_together=set([('user', 'answer')]),
        ),
    ]
