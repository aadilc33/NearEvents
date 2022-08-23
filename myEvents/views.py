from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def myEvents(request):
    return render(request,"myEvents.html")
