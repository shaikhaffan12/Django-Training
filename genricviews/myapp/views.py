from urllib import request
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializer import StudentSerializer

# Create your views here.
class My_Student (ListModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs)

class My_StudentCreate (CreateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)

class My_StudentRetrieve (RetrieveModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

class My_StudentUpdate (UpdateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request,*args, **kwargs)

class My_StudentDelete(DestroyModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)