# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-20 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='legal_name',
        ),
    ]
