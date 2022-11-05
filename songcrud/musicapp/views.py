from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Artiste, Song, Lyrics
from rest_framework import routers, serializers, viewsets, request





# Create your views here.
'''@api_view(['GET'])
def getData(request):
    queryset = Song.objects.all()
    serializer = SongSerializer(queryset, many=True)

    return(serializer.data)'''
class SongViews(generics.CreateAPIView):
    queryset =Song.objects.all()
    serializer_class =SongSerializer


class GetSongviews(generics.ListAPIView):
    queryset =Song.objects.all()
    serializer_class =SongSerializer

class ArtisteViews(generics.CreateAPIView):
    queryset =Song.objects.all()
    serializer_class =SongSerializer


class GetArtisteviews(generics.ListAPIView):
    queryset =Song.objects.all()
    serializer_class =SongSerializer


class lyricsViews(generics.CreateAPIView):
    queryset =Song.objects.all()
    serializer_class =SongSerializer


class Getlyricsviews(generics.ListAPIView):
    queryset =Song.objects.all()
    serializer_class =SongSerializer