from django.shortcuts import render

from django.http import HttpResponse

from app.models import *

from app.forms import *

# Create your views here.

def insert_topic(request):
    TFO=TOPICFORM()
    d={'TFO':TFO}
    if request.method=='POST':
        TFDO=TOPICFORM(request.POST)
        if TFDO.is_valid():
           TFDO.save()
        return HttpResponse ('insert_topic is inserted succesfully ')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WFO=WEBPAGEFORM()
    d={'WFO':WFO}
    if request.method=='POST':
        WPO=WEBPAGEFORM(request.POST)
        if WPO.is_valid():
           WPO.save()
        return HttpResponse ('insert_webpage is inserted succesfully ')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AR=ACCESSFORM()
    d={'AR':AR}

    if request.method=='POST':
        ARO=ACCESSFORM(request.POST)
        if ARO.is_valid():
            ARO.save()
            return HttpResponse ('insert_access is inserted succesfully')

    return render(request,'insert_access.html',d)
