from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField


class ImageCarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.TextBlock(required=False)

    class Meta:
        icon = 'image'


class GoogleMapBlock(blocks.StructBlock):
    map_long = blocks.CharBlock(required=True, max_length=255)
    map_lat = blocks.CharBlock(required=True, max_length=255)
    map_zoom_level = blocks.CharBlock(default=14, required=True, max_length=3)

    class Meta:
        template = 'content_page/blocks/google_map.html'
        icon = 'cogs'
        label = 'Google Map'


COLOUR_CHOICES = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
]


class TwoColumnBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, required=False)
    left_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('image_carousel', blocks.ListBlock(ImageCarouselBlock(), template='content_page/blocks/carousel_small.html')),

        ('embedded_video', EmbedBlock()),
        ('google_map', GoogleMapBlock()),
    ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('image_carousel', blocks.ListBlock(ImageCarouselBlock(), template='content_page/blocks/carousel_small.html')),
        ('embedded_video', EmbedBlock()),
        ('google_map', GoogleMapBlock()),
    ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'content_page/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class ThreeColumnBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, default="white")
    left_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('image_carousel', blocks.ListBlock(ImageCarouselBlock(), template='content_page/blocks/carousel_small.html')),
        ('embedded_video', EmbedBlock()),
        ('google_map', GoogleMapBlock()),
    ], icon='arrow-left', label='Left column content')

    middle_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('image_carousel', blocks.ListBlock(ImageCarouselBlock(), template='content_page/blocks/carousel_small.html')),
        ('embedded_video', EmbedBlock()),
        ('google_map', GoogleMapBlock()),
    ], icon='arrow-up', label='Middle column content')

    right_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('image_carousel', blocks.ListBlock(ImageCarouselBlock(), template='content_page/blocks/carousel_small.html')),
        ('embedded_video', EmbedBlock()),
        ('google_map', GoogleMapBlock()),
    ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'content_page/blocks/three_column_block.html'
        icon = 'placeholder'
        label = 'Three Columns'


class ContentPage(Page):
    intro = models.CharField(max_length=255, null=True, blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image")),

        ('two_columns', TwoColumnBlock()),
        ('three_columns', ThreeColumnBlock()),
        ('embedded_video', EmbedBlock(icon="media")),
        ('google_map', GoogleMapBlock()),
        ('image_carousel', blocks.ListBlock(ImageCarouselBlock(), template='content_page/blocks/carousel.html', icon="image")),

    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]