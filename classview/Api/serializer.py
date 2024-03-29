from rest_framework import serializers
from Api.models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)