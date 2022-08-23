from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import event
import json
import os
def index(request):
    t = []
    temp = {}
    # events = event.objects.all()
    filename = os.path.join(os.getcwd()+"\events\static\json\\test.json")
    with open(filename, 'r') as f:
        event_list = json.loads(f.read())
        print(event_list['test'])
    print(type (event_list))
    # qs_json = serializers.serialize('json', events)
    # qs_json =(json.loads(qs_json))
    #
    # for i in qs_json:
    #     t .append(i['fields'])
    # s = data['test']+t
    # temp['test'] =s
    # # test['test']=s
    # print(json.dumps(temp))
    # event_list = event.objects.all()
    return render(request,'index.html',{"event_list":event_list['test']})

