from django.conf.urls import patterns, url
from .views import EventListView, EventDetailView


urlpatterns = patterns('',
    url(r'$', EventListView.as_view(), name='events_list'),
    url(r'(?P<pk>\d+)/$', EventDetailView.as_view(), name='event_details'),
)
