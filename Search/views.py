from django.http import HttpResponse
from django.shortcuts import render
import os
import json
# Create your views here.

def search(request):
    filename = os.path.join(os.getcwd() + "\events\static\json\\test.json")
    with open(filename, 'r') as f:
        data = json.loads(f.read())
    print(type(data))
    s = data['test']
    print(type(s))
    return render(request,"search.html",data)
