from .models import Student
from rest_framework import serializers

#model serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        

        