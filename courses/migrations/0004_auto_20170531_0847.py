# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170529_0347'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Step',
            new_name='Text',
        ),
    ]
