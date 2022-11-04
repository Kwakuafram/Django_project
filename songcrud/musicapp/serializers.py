from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Artiste, Song, Lyrics


class ArtisteSerializer(serializers.serializer):
    class meta:
        model = Artiste
        field = "__all__"




class SongSerializer(serializers.serializer):
    class meta1:
        model = Song
        field = "__all__"



        
class LyricSerializer(serializers.serializer):
    class meta2:
        model = Lyrics
        field = "__all__"