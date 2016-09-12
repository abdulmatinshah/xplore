# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 15:52
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('content_page', '0002_auto_20160910_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('two_columns', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')], default='white')), ('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)))))), icon='arrow-left', label='Left column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)))))), icon='arrow-right', label='Right column content'))))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)))))), blank=True, null=True),
        ),
    ]