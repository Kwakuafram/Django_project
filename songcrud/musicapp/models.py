from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField
    
    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=200)
    date_release = models.DateTimeField
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Lyrics(models.Model):
    content = models.CharField(max_length=500)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
         return self.content