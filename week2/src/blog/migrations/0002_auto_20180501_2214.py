# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-01 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tilte',
            new_name='title',
        ),
    ]
