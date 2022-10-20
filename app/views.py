import imp
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
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
    W=Webpage.objects.filter(name__startswith='s')
    W=Webpage.objects.filter(name__endswith='n')
    W=Webpage.objects.filter(name__contains='s')
    W=Webpage.objects.filter(name__in=('pawan','ashu'))
    W=Webpage.objects.filter(name__regex='\w{8}')
    W=Webpage.objects.filter(Q(topic_name='Cricket') | Q(topic_name='Chess'))
    W=Webpage.objects.all()
    
    d={'webpages':W}
    return render(request,'display_webpage.html',d)

def display_access(request):
    A=AccessRecords.objects.all()
    A=AccessRecords.objects.filter(date__year=1999)
    A=AccessRecords.objects.filter(date__month=10)
    A=AccessRecords.objects.filter(date__day=10)
    A=AccessRecords.objects.filter(date='1998-07-10')
    A=AccessRecords.objects.filter(date__gt='1998-07-10')
    A=AccessRecords.objects.filter(date__gte='1998-07-10')
    A=AccessRecords.objects.filter(date__lte='1999-10-26')
    A=AccessRecords.objects.filter(date__year__gt='1999')
    
def update_webpage(request):
    #Webpage.objects.filter(topic_name='Cricket').update(name='Virat')
    #Webpage.objects.filter(topic_name='Volley Ball').update(name='Kabir')
    #Webpage.objects.filter(name='basha').update(topic_name='Cricket')
    #Webpage.objects.filter(name='basha shaik').update(topic_name='Cricket')
    #Webpage.objects.update_or_create(topic_name='Chess',defaults={'name':'Charan Kumar','url':'https://charan.in'})
    #Webpage.objects.update_or_create(topic_name='Cricket',defaults={'name':'MSD','url':'https://MSD.in'})
    T=Topic.objects.get_or_create(topic_name='Cricket')[0]
    T.save()
    Webpage.objects.update_or_create(name='Kiran',defaults={'topic_name':T,'url':'https://kiran.in'})
    W=Webpage.objects.all()
    d={'webpages':W}
    return render(request,'display_webpage.html',d)



def delete_webpage(request):
    #Webpage.objects.filter(topic_name='Volley Ball').delete()
    Webpage.objects.all().delete()

    W=Webpage.objects.all()
    d={'webpages':W}
    return render(request,'display_webpage.html',d)











    
    
    
    
    
    
    d={'access':A}
    return render(request,'display_access.html',d)






