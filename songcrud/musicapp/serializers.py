from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Artiste, Song, Lyrics


class ArtisteSerializer(serializers.ModelSerializer):
    class meta:
        model = Artiste
        field = "__all__"


    def create(self, validated_data):
        return super().create(validated_data)




class SongSerializer(serializers.Serializer):
    class meta1:
        model = Song
        field = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)



        
class LyricSerializer(serializers.ModelSerializer):
    class meta2:
        model = Lyrics
        field = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)