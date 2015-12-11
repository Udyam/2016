from django.db import models
from django.utils.encoding import smart_unicode
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import RegexValidator

# Create your models here.

tenDigitContact = RegexValidator(r'^\d{10,10}$')


class JSONField(models.TextField):
    """
    JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly.
    Django snippet #1478

    example:
        class Page(models.Model):
            data = JSONField(blank=True, null=True)


        page = Page.objects.get(pk=5)
        page.data = {'title': 'test', 'type': 3}
        page.save()
    """
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if value == "":
            return None

        try:
            if isinstance(value, basestring):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return super(JSONField, self).get_db_prep_save(value, *args, **kwargs)


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
class RegistrationInfo(models.Model):
    event_name = models.ForeignKey(Events)
    team_name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    contact = models.IntegerField(blank=False, null=False, validators=[tenDigitContact])
    team_detail = JSONField(blank=False, null=False)
