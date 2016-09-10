from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                InlinePanel)

# from blog.models import BlogPost


class SlideshowImage(models.Model):
    picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('picture'),
    ]


class SlideshowSlideshowImage(Orderable, SlideshowImage):
    slideshow_picture = ParentalKey('Homepage', related_name='slideshow_images')


class HomePage(Page):
    body = RichTextField(blank=True)

    # @property
    # def posts(self):
    #     return BlogPost.objects.order_by('-date')[:3]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('slideshow_images', label="Slideshow Images"),
    ]
