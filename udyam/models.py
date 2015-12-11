from django.db import models
from django.utils.encoding import smart_unicode
from django.core.validators import RegexValidator

import json

tenDigitContact = RegexValidator(r'^\d{10,10}$')


class RegistrationInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=20, blank=False, null=False)
    team_name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    contact = models.IntegerField(blank=False, null=False, validators=[tenDigitContact])
    team_details = models.TextField(blank=False, null=False)
