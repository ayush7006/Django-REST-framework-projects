from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

#class based view

from rest_framework.views import APIView  
class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk                                  #id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)
    def put(self,request,pk=None,format=None):
        id = pk                                  #id = request.data.get('id')
        stu = Student.objects.get(pk=id) 
        serializer = StudentSerializer(stu ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complit data updated'})
        return Response(serializer.errors)
    def patch(self,request,pk=None,format=None):
        id = pk                                  #id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu ,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' PATCH data updated'})
        return Response(serializer.errors)
    def delete(self,request,pk=None,format=None):
        id = pk                                  #id = request.data.get('id') 
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})


# function baesd view
#from rest_framework.decorators import api_view
'''
@api_view(['GET','POST','PUT','PATCH','DELETE'])   #patch added
def Student_api(request,pk=None):
    if request.method == 'GET':
        id = pk                                  #id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk                                  #id = request.data.get('id')
        stu = Student.objects.get(pk=id) 
        serializer = StudentSerializer(stu ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complit data updated'})
        return Response(serializer.errors)


    if request.method == 'PATCH':
            id = pk                                  #id = request.data.get('id')
            stu = Student.objects.get(pk=id) 
            serializer = StudentSerializer(stu ,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':' PATCH data updated'})
            return Response(serializer.errors)




    if request.method == 'DELETE':
        id = pk                                  #id = request.data.get('id') 
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'}) 
'''