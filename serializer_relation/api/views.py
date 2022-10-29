from django.shortcuts import render
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets
from .models import Singer, Song
# Create your views here.\

class SingerViewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer    
