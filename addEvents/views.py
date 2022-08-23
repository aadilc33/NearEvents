from django.contrib import messages
from django.shortcuts import render
from events.models import *
from django.utils import timezone
from .AddEventForm import VenueForm
from django.http import HttpResponseRedirect
# Create your views here.

def addVenue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request succeded successfuly')
            return render(request,'addV.html/',{"form": VenueForm})
        else:
            messages.error(request, 'Invalid form submission')
            messages.error(request, form.errors)
            return render(request, "addV.html/", {"form": form, 'submitted': submitted})
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request,"addV.html/",{"form":form,'submitted':submitted})



def addEvents(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Request succeded successfuly')
            return HttpResponseRedirect('addV?submitted=True')
        else:
            messages.error(request,'Invalid form submission')
            messages.error(request, form.errors)

    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request,"addV",{"venue form":form})