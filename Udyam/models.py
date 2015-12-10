from django.db import models
from django.utils.encoding import smart_unicode
from django.core.validators import RegexValidator

# Create your models here.

tenDigitContact = RegexValidator(r'^\d{10,10}$')


class Events(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False, help_text="Please '_' in place of space")
    min_member = models.SmallIntegerField(null=True, default=1, verbose_name="Minimum team members allowed")
    max_member = models.SmallIntegerField(null=False, verbose_name="Maximum team members allowed")

    def save(self, *args, **kwargs):
        self.name = self.name.replace(" ", "_")
        super(Events, self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_unicode(self.name.replace('_', ' '))


# TODO changes can be done, not yet final, error messages to be added
class Team(models.Model):
    event_name = models.ForeignKey(Events)
    team_name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    name1 = models.CharField(max_length=60, blank=False, null=False)
    email1 = models.EmailField(max_length=100, blank=False, null=False)
    contact1 = models.IntegerField(blank=False, null=False, validators=[tenDigitContact])
    name2 = models.CharField(max_length=60, blank=False, null=False)
    email2 = models.EmailField(max_length=100, blank=False, null=False)
    contact2 = models.IntegerField(blank=False, null=False, validators=[tenDigitContact])
    name3 = models.CharField(max_length=60, blank=False, null=False)
    email3 = models.EmailField(max_length=100, blank=False, null=False)
    contact3 = models.IntegerField(blank=False, null=False, validators=[tenDigitContact])
    name4 = models.CharField(max_length=60, blank=False, null=False)
    email4 = models.EmailField(max_length=100, blank=False, null=False)
    contact4 = models.IntegerField(blank=False, null=False, validators=[tenDigitContact])
