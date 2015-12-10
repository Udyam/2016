from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.


class Events(models.Model):
    name = models.CharField(max_length=20, unique= True, blank=False, help_text="Please '_' in place of space")
    min_member = models.SmallIntegerField(null=True, default=1, verbose_name="Minimum team members allowed")
    max_member = models.SmallIntegerField(null=False, verbose_name="Maximum team members allowed")

    def save(self, *args, **kwargs):
        self.name = self.name.replace(" ", "_")
        super(Events, self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_unicode(self.name.replace('_', ' '))


class Team(models.Model):
    event_name = models.ForeignKey(Events)
    # TODO complete this
