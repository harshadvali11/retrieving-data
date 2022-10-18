import imp
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    T=Topic.objects.all()
    d={'topics':T}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    W=Webpage.objects.all()
    #W=Webpage.objects.filter(topic_name='Cricket')
    #W=Webpage.objects.exclude(topic_name='Cricket')
    W=Webpage.objects.all().order_by('name')
    W=Webpage.objects.all().order_by('-name')
    W=Webpage.objects.filter(topic_name='Volley Ball').order_by('name')
    W=Webpage.objects.filter(topic_name='Cricket')
    W=Webpage.objects.order_by(Length('name'))
    W=Webpage.objects.order_by(Length('name').desc())
    W=Webpage.objects.all()[:4:]
    d={'webpages':W}
    return render(request,'display_webpage.html',d)

def display_access(request):
    A=AccessRecords.objects.all()
    d={'access':A}
    return render(request,'display_access.html',d)






