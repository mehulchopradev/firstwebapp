from rest_framework import serializers
from library.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username', 'password', 'gender', 'country')
