# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-06 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_app', '0002_auto_20161106_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genericobject',
            name='objtimestamp',
        ),
        migrations.AlterField(
            model_name='genericobject',
            name='updated_at',
            field=models.DateTimeField(default='2016-11-06T10:46:15'),
        ),
    ]
