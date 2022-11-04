from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from songcrud.musicapp.serializers import SongSerializer
from .models import Artiste, Song, Lyrics
from rest_framework import routers, serializers, viewsets





# Create your views here.
class getsongview(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
