from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *
# Create your views here.
def topicfun(request):
    TDO=topicform()
    d={'TDO':TDO}
    if request.method=='POST':
        TO=topicform(request.POST)
        if TO.is_valid():
            TO.save()
            return HttpResponse('DATA INSERTED SUCCESSFULLY')
    return render(request,'topic.html',d)

def webpagesfun(request):
    WDO=webpagesform()
    d={'WDO':WDO}
    if request.method=='POST':
        WO=webpagesform(request.POST)
        if WO.is_valid():
            WO.save()
            return HttpResponse('DATA INSERTED SUCCESSFULLY')
    return render(request,'webpages.html',d)

def accessrecordsfun(request):
    ADO=accessrecordsform()
    d={'ADO':ADO}
    if request.method=='POST':
        AO=accessrecordsform(request.POST)
        if AO.is_valid():
            AO.save()
            return HttpResponse('DATA INSERTED SUCCESSFULLY')
    return render(request,'accessrecords.html',d)