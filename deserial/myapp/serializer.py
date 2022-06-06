from rest_framework import serializers
from .models import student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)
    roll_no = serializers.IntegerField()

    def create(self, validate_data):
        return student.objects.create(**validate_data)