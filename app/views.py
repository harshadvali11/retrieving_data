from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='Cricket')
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='Cricket')
    QSW=Webpage.objects.exclude(topic_name='Cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.order_by('-name')
    QSW=Webpage.objects.filter(topic_name='Kabaddi').order_by('-name')    
    QSW=Webpage.objects.all().order_by(Length('name'))    
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    
    QSW=Webpage.objects.filter(name__startswith='D')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__contains='d')    
    QSW=Webpage.objects.filter(name__regex='\w{7}')
    QSW=Webpage.objects.filter(name__in=['Dhoni','damodhar','Vishnu'])
    QSW=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name='Vishnu'))
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(Q(topic_name='Rugby') & Q(url__startswith='https'))
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)
    
def display_access(request):
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='1998-08-10')    
    QSA=AccessRecords.objects.filter(date__gt='1998-08-10')    
    QSA=AccessRecords.objects.filter(date__gte='1998-08-10') 
    QSA=AccessRecords.objects.filter(date__lte='1998-08-10')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year='1998')  
    QSA=AccessRecords.objects.filter(date__month='8')    
    QSA=AccessRecords.objects.filter(date__day='10')   
    QSA=AccessRecords.objects.filter(date__year__gt='1998')
    d={'access':QSA}
    return render(request,'display_access.html',d)


def update_webpage(request):
    #Webpage.objects.filter(name='basha123').update(url='https://basha.in')
    #Webpage.objects.filter(topic_name='Cricket').update(name='MSD')
    #Webpage.objects.filter(name='basha').update(topic_name='Cricket')
    #Webpage.objects.filter(name='pawan').update(topic_name='Hockey')
    #Webpage.objects.update_or_create(name='suresh',defaults={'url':'https://suresh.in'})
    #Webpage.objects.update_or_create(name='MSD',defaults={'url':'https://MSD.in'})
    T=Topic.objects.get_or_create(topic_name='Cricket')[0]
    T.save()
    Webpage.objects.update_or_create(name='ashu',defaults={'topic_name':T,'url':'https://suresh.in'})

    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)


def delete_webpage(request):
    #Webpage.objects.filter(name='Abcdefg').delete()
    #Webpage.objects.filter(topic_name='Cricket').delete()
    #Webpage.objects.filter(name='aravindh').delete()
    Webpage.objects.all().delete()
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)





















