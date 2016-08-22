from __future__ import absolute_import, print_function, unicode_literals

import logging

from django.template import Library

from woyd.models import NavigationMenu, Service

register = Library()
logger = logging.getLogger(__name__)


@register.assignment_tag(takes_context=False)
def load_navigation_menu(location):
    try:
        return NavigationMenu.objects.get_by_natural_key(location)
    except NavigationMenu.DoesNotExist:
        logger.critical("No such navigation menu %s", location)


@register.inclusion_tag('partials/services.html', takes_context=True)
def services(context):
    return {
        'services': Service.objects.all(),
        'request': context['request'],
    }
