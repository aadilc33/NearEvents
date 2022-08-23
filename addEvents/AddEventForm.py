from django import forms
from django.forms import ModelForm
from location.models import Venue
from events.models import event


class VenueForm(ModelForm):
   class Meta:
      model = Venue
      fields = ('name','address','zip_code','phone','Web','email_address')


class AddEventsForm(forms.ModelForm):

   class Meta:
      model = event
      fields = ('name','venue','category')
