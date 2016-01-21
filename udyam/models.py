from django.db import models
from django.utils.encoding import smart_unicode

import json

class RegistrationInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=20, blank=False, null=False)
    team_name = models.CharField(max_length=50, blank=False, null=False)
    contact = models.CharField(max_length=200, blank=False, null=False)
    team_details = models.TextField(blank=False, null=False)

    class Meta:
        unique_together = ('event_name', 'team_name')

    def __unicode__(self):
        _details = json.loads(self.contact)
        return smart_unicode(self.team_name + ":" + _details['contact'] + ":" + _details['name'] + ": " + _details['email'])