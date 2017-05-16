# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-10 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtailblocks_cards.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitySnippetPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', wagtail.wagtailcore.fields.StreamField((('home_block', wagtail.wagtailcore.blocks.StructBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('linktext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('videolink', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('videotext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formh3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('ortext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('button', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formtext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formlink', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('formlinktext', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('features_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('sub', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('features_item', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)))))))))), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('features_alt_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Картина слева или справа?'), ('left', 'Слева'), ('right', 'Справа')], required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('btnlink', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('price_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('price', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('duration', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btnlink', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('fields', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False))))))))))))), ('clients_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('clients_list', wagtailblocks_cards.blocks.CardsBlock(wagtail.wagtailcore.blocks.StructBlock((('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)))))), ('blocks', wagtailblocks_cards.blocks.CardsBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('company', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('city', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))))))), ('subscribe_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('smalltext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('our_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Картина слева или справа?'), ('left', 'Слева'), ('right', 'Справа')], required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))), ('solutions_block', wagtail.wagtailcore.blocks.StructBlock((('h5', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h2', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Блок светлый или тёмный?'), ('light', 'Светлый'), ('dark', 'Тёмный')], required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formh3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('button', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('story_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)))))), blank=True, verbose_name='Сниппет для страницы городов')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.City')),
            ],
        ),
        migrations.AlterField(
            model_name='citypage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('home_block', wagtail.wagtailcore.blocks.StructBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('linktext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('videolink', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('videotext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formh3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('ortext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('button', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formtext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formlink', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('formlinktext', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('features_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('sub', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('features_item', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)))))))))), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('features_alt_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Картина слева или справа?'), ('left', 'Слева'), ('right', 'Справа')], required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('btnlink', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('price_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('price', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('duration', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btnlink', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('fields', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False))))))))))))), ('clients_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('clients_list', wagtailblocks_cards.blocks.CardsBlock(wagtail.wagtailcore.blocks.StructBlock((('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)))))), ('blocks', wagtailblocks_cards.blocks.CardsBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('company', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('city', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))))))), ('subscribe_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('smalltext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('our_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Картина слева или справа?'), ('left', 'Слева'), ('right', 'Справа')], required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))), ('solutions_block', wagtail.wagtailcore.blocks.StructBlock((('h5', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h2', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Блок светлый или тёмный?'), ('light', 'Светлый'), ('dark', 'Тёмный')], required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formh3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('button', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('story_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)))))), blank=True, verbose_name='Home content block'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('home_block', wagtail.wagtailcore.blocks.StructBlock((('h1', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('linktext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('videolink', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('videotext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formh3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('ortext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('button', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formtext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formlink', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('formlinktext', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('features_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('sub', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('features_item', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)))))))))), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('features_alt_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Картина слева или справа?'), ('left', 'Слева'), ('right', 'Справа')], required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('btnlink', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('price_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('price', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('duration', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btnlink', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('fields', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False))))))))))))), ('clients_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('clients_list', wagtailblocks_cards.blocks.CardsBlock(wagtail.wagtailcore.blocks.StructBlock((('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)))))), ('blocks', wagtailblocks_cards.blocks.CardsBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('company', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('city', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))))))), ('subscribe_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('smalltext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('our_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Картина слева или справа?'), ('left', 'Слева'), ('right', 'Справа')], required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))), ('solutions_block', wagtail.wagtailcore.blocks.StructBlock((('h5', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h2', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Блок светлый или тёмный?'), ('light', 'Светлый'), ('dark', 'Тёмный')], required=False)), ('btntext', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('formh3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('button', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('handle', wagtail.wagtailcore.blocks.CharBlock())))), ('story_block', wagtail.wagtailcore.blocks.StructBlock((('h3', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('h4', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Иконки можно брать любые. Писать целиком класс, например fa fa-user или pe-7s-rocket', required=False)))))), blank=True, verbose_name='Home content block'),
        ),
    ]