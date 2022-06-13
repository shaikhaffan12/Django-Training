from django.shortcuts import render
from rest_framework.response import Response
from .models import Student1
from .serializer import StudentSerializer1
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class modelview(viewsets.ModelViewSet):
    queryset = Student1.objects.all()
    serializer_class = StudentSerializer1