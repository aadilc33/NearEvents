from django.contrib import admin
from .models import  *
from django.contrib.auth.models import User
# Register your models here.
@admin.register(MyclubUsers)
class MyclubUsersAdmin(admin.ModelAdmin):
    list_display = ('first_name',"last_name","email")
    ordering = ("first_name","last_name")
    search_fields = ("first-name","last_name")