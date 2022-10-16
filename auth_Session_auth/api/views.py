#model view et mehtod
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions



class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [DjangoModelPermissions]
    #permission_classes = [IsAuthenticatedOrReadOnly]

# HOW TO USE FUNCTON AUTH
# 1 imports requred 
# 2 @authentication_classes([SessionAuthentication])
# 2 @permission_classes([IsAuthenticated])


# view set method
'''
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

class StudentViewset(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id=pk 
        if id is not None:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    def partial_update(self,request,pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu ,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors) 
    def destory(self,request,pk):
        id = pk 
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data--delete'})
        '''
