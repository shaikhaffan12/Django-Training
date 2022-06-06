from django.shortcuts import render
from .models import student
from serail1.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def serilizeJson(request):
    data = student.objects.all()
    serialize = StudentSerializer(data,many=True)
    print(serialize.data)
    json_data = JSONRenderer().render(serialize.data)
    return HttpResponse(json_data,content_type='application/json')

# def serilizeJsonlist(request, pk):
#     data = student.objects.get(id = pk)
#     serialize = StudentSerializer(data,many=True)
#     print(serialize.data)
#     json_data = JSONRenderer().render(serialize.data)
#     return HttpResponse(json_data,content_type='application/json')
    