# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-20 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('companies', '0003_auto_20171220_2001'),
        ('account', '0002_email_max_length'),
        ('socialaccount', '0003_extra_data_default_dict'),
        ('users', '0002_auto_20171219_0624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clearbituser',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='ClearbitUser',
        ),
    ]
