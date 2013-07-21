from django.db import models
from django.utils.translation import ugettext as _
from filer.fields.image import FilerImageField

from model_utils.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    def __unicode__(self):
        return self.name


class Event(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'))
    event_start = models.DateTimeField(_('Start time'), blank=True)
    event_end = models.DateTimeField(_('End time'), blank=True)
    location = models.CharField(_('Location'), max_length=50, blank=True)
    image = FilerImageField(null=True, blank=True, default=None, verbose_name=_("Image"))
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ['-event_start']

    @models.permalink
    def get_absolute_url(self):
        return 'event_details', (), {'pk': self.pk}

    def __unicode__(self):
        return self.title 
