from django.shortcuts import render
from GenericApp.models import Student1
from GenericApp.serializer import StudentSerializer1
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student1.objects.all()
    serializer_class = StudentSerializer1