from django.db import models
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=50)


class Event(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'))
    event_start = models.DateTimeField(_('Start time'))
    event_end = models.DateTimeField(_('End time'))
    location = models.CharField(_('Location'), max_length=50)
    image = models.ImageField(_('Image'))

    class Meta:
        order_by = '-event_start'

    @models.permalink
    def get_absolute_url(self):
        return 'event_details', (), {'pk': self.pk}