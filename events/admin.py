from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

admin.site.register(ClubUsers)


@admin.register(Events)
class EventsAdmin(ModelAdmin):
    list_display = ['name', 'event_date', 'venue']
    list_filter = ('name', 'venue')
    search_fields = ('name',)
    fields = ('name', ('event_date', 'event_time'), 'venue', ('attendees', 'manager'),)


@admin.register(Venue)
class VenueAdmin(ModelAdmin):
    list_display = ['name', 'address']
    fields = ('name', ('address', 'zip_code'), ('phone_number', 'web_address', 'email_address'),)
    ordering = ('name',)
