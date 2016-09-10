# from __future__ import unicode_literals
#
# from django.db import models
#
# from wagtail.wagtailcore.models import Page
# from wagtail.wagtailcore.fields import RichTextField
# from wagtail.wagtailadmin.edit_handlers import FieldPanel
# from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
# from wagtail.wagtailsearch import index
#
#
# class BlogPost(Page):
#     main_image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#     date = models.DateTimeField('Date')
#     intro = models.CharField(max_length=250)
#     body = RichTextField(blank=True)
#
#     search_fields = Page.search_fields + [
#         index.SearchField('intro'),
#         index.SearchField('body'),
#     ]
#
#     content_panels = Page.content_panels + [
#         FieldPanel('date'),
#         ImageChooserPanel('main_image'),
#         FieldPanel('intro'),
#         FieldPanel('body'),
#     ]
#
#     class Meta:
#         ordering = ['-date']
#
#
# class BlogIndex(Page):
#     intro = RichTextField(blank=True)
#
#     content_panels = Page.content_panels + [
#         FieldPanel('intro', classname="full"),
#     ]
#
#     @property
#     def posts(self):
#         return BlogPost.objects.order_by('-date')
