Events plugin for django-cms
===============================

MVP:
----
It allows the grouping of events into categories.
Events can be listed, and detail views can be given.
Events from a given category can be listed.

Extras:
--------
ical, gcalendar integration
facebook event creation

Installation
-------------

1. add `cmsplugin_events` to INSTALLED_APPS
2. syncdb and migrate
3. create a new page, and set the Event application to handle that page
4. create events in the admin
   
Optionally add the Event listings plugin to other pages.