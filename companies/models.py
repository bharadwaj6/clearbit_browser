from __future__ import unicode_literals

from django.db import models

from clearbit_browser.users.models import User


class Company(models.Model):
    user = models.ForeignKey(User)
    clearbit_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    updated_at = models.DateTimeField()
    logo_url = models.TextField(null=True)
