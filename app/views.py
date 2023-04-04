from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.models import *

def insert_topic(request):

   tn=input('enter topic_name')
   TO=Topic.objects.get_or_create(tname=tn)[0]
   TO.save()
   return HttpResponse('Topic date insert successfully')
def insert_webpages(request):
   tn=input('enter tn')
   n=input('enter name')
   url=input('enter url')
   

   TO=Topic.objects.get_or_create(tname=tn)[0]
   TO.save()

   WO=Webpages.objects.get_or_create(tname=TO,name=n,url=url)[0]
   WO.save()

   return HttpResponse('Webpages data is inserted')
def insert_accessrecord(request):
   tn=input('enter topic_name')
   n=input('enter name')
   url=input('enter url')

   ar=input('enter author')
   d=input('enter date')


   TO=Topic.objects.get_or_create(tname=tn)[0]
   TO.save()

   WO=Webpages.objects.get_or_create(tname=TO,name=n,url=url)[0]
   WO.save()

   AO=AccessRecord.objects.get_or_create(name=WO,author=ar,date=d)[0]
   AO.save()

   return HttpResponse('AccessRecord data is insert in successfully....!')


   


