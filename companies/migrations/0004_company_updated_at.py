# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-20 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20171220_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
