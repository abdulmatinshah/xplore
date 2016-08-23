from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                InlinePanel,
                                                PageChooserPanel)
from wagtail.wagtailcore.fields import RichTextField


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(null=True, blank=True,
                               help_text='Your Facebook page URL')
    pinterest = models.URLField(null=True, blank=True,
                                help_text='Your Pinterest page URL')
    twitter = models.URLField(null=True, blank=True,
                              help_text='Your Twitter page URL')
    instagram = models.URLField(null=True, blank=True,
                                help_text='Your Instagram page URL')
    youtube = models.URLField(null=True, blank=True,
                              help_text='Your YouTube channel or user account URL')


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def url(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class NavigationMenuItem(Orderable, LinkFields):
    menu = ParentalKey(to='woyd.NavigationMenu', related_name='menu_items')
    menu_title = models.CharField(max_length=255, blank=True, null=True,
                                  help_text="Optional link title in this menu (defaults to page title if one exists)")

    @property
    def menu_item_title(self):
        if self.menu_title:
            return self.menu_title
        if self.link_page:
            return self.link_page.title
        elif self.link_document:
            return self.link_document.title
        else:
            return self.link_external

    def __str__(self):
        return self.menu_item_title

    panels = [FieldPanel('menu_title')] + LinkFields.panels


class NavigationMenuManager(models.Manager):
    def get_by_natural_key(self, menu_location):
        return self.get(menu_location=menu_location)


@register_snippet
class NavigationMenu(ClusterableModel):
    objects = NavigationMenuManager()
    menu_location = models.CharField(null=False, max_length=255, help_text="Template name (do not change)", unique=True)
    menu_name = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        name = self.menu_name
        if not name:
            name = "Unnamed"

        return "{name} ({location})".format(name=name, location=self.menu_location)

NavigationMenu.panels = [
    FieldPanel('menu_name'),
    InlinePanel('menu_items', label="Linked Pages"),
    FieldPanel('menu_location')
]


@register_snippet
class Service(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(blank=True)
    picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
        ImageChooserPanel('picture'),
        PageChooserPanel('link_page'),
    ]

    def __str__(self):
        title = self.title
        if not title:
            title = 'Untitled service'

        return title
