from rest_framework import serializers
from .models import Student1

class StudentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = '__all__'