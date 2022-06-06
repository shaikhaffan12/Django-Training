from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)
    roll_no = serializers.IntegerField()