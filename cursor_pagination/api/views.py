from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer 
from rest_framework.generics import ListAPIView
from .paginations import MYCP

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MYCP