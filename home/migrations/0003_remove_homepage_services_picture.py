# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 13:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_services_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='services_picture',
        ),
    ]
