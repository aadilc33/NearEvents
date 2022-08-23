from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def eventsDetails(request):
    # context = {"test":(request.POST.get('pizza'))}

    return render(request,"eventDetails.html" )
