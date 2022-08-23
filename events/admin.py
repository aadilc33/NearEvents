from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
admin.site.register(imageStore)

class EventInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = event

@admin.register(event)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('event_name','category','description','telephone','date_time','pImage')
    fields = (('name','venue'),'category','date_time','manager')
    list_display = ('name','venue','category','date_time','manager')
    list_filter = ('date_time','venue')
    ordering = ('name','date_time')



