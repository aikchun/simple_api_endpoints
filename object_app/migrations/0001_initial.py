# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-28 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objkey', models.CharField(max_length=30)),
                ('objvalue', models.TextField()),
                ('objtimestamp', django_unixdatetimefield.fields.UnixDateTimeField()),
            ],
            options={
                'verbose_name_plural': 'GenericObjects',
                'verbose_name': 'GenericObject',
            },
        ),
    ]