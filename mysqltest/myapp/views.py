from django.shortcuts import render
from django.http import HttpResponse
from .models import person
from datetime import datetime

# Create your views here.
def posthere(request):
    first_name = 'rohit'
    last_name = 'ghule'
    date = datetime.now()
    Person = person(first_name=first_name,last_name=last_name,date=date)
    Person.save()
    return HttpResponse("submitted")

def updatehere(request,pk):
    Person = person.objects.get(id=pk)
    print(Person)
    Person.last_name = "abc"
    person.date = datetime.now()
    Person.save()
        
    return HttpResponse('submmited')