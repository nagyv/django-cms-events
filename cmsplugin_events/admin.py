from django.contrib import admin
from .models import Event, Category

class EventAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('title', 'event_start', 'event_end', 'location', 'category')

admin.site.register(Category)
admin.site.register(Event, EventAdmin)