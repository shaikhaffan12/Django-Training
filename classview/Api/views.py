from urllib import response
from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from Api.serializer import StudentSerializer
from Api.models import Student
from django.shortcuts import get_object_or_404

# Create your views here.

class my_class(APIView):
    def get(self,request, pk = None):
        if pk is not None:
            student = Student.objects.get(pk = pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        student = Student.objects.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)

        
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Data Created.')
        else:
            return HttpResponse('Error Occured')

    def put(self, request, pk):
        saved_article = Student.objects.get(pk=pk)
        serializer = StudentSerializer(saved_article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def patch(self, request, pk):
        saved_article = Student.objects.get(pk=pk)
        serializer = StudentSerializer(saved_article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id=None):
        result = get_object_or_404(Student, id=id)
        result.delete()
        return Response({"status": "success", "data": "Record Deleted"})

        #end 