import random
from sekizai.context import SekizaiContext
from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import EventListPlugin, Event

class EventList(CMSPluginBase):
    model = EventListPlugin
    name = _('Event list')
    render_template = 'cmsplugin_events/event_list_plugin.html'

    def render(self, context, instance, placeholder):
        object_list = Event.ongoing.all()
        if instance.category:
            object_list = object_list.filter(category=instance.category)
        return SekizaiContext({
            'object_list': object_list,
            'instance': instance
            })
plugin_pool.register_plugin(EventList)
