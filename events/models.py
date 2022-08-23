from django.db import models
import os
import uuid
from register.models import MyclubUsers
from django.urls import reverse  # To generate URLS by reversing URL patterns
from location.models import Venue
from register.models import MyclubUsers
from NearEvent import settings
from django.contrib.auth.models import User


class imageStore(models.Model):
    pImage = models.ImageField(help_text="Enter Pimage", upload_to=str(settings.BASE_DIR) + "/static/media/uploaded")
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class event(models.Model):
    name = models.CharField(max_length=120)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, help_text="Enter Category")
    description = models.CharField(max_length=350, help_text="Enter Description")
    date_time = models.DateTimeField(help_text="Enter date of event")
    pImage = models.ForeignKey(imageStore, on_delete=models.CASCADE, blank=True, null=True)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, max_length=60)
    attendes = models.ManyToManyField(MyclubUsers, blank=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('event-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
