"""songcrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
#from django.contrib import views

from django.urls import path, include

urlpatterns = [
    path('song', views.SongViews.as_view(), name='song'),
    path('get-song', views.GetSongviews.as_view(), name='get-song'),
    
    path('Artiste', views.ArtisteViews.as_view(), name='Artiste'),
    path('get-Artiste', views.GetArtisteviews.as_view(), name='get-Artiste'),

    
    path('lyric', views.lyricsViews.as_view(), name='lyrics'),
    path('get-lyrics', views.Getlyricsviews.as_view(), name='get-lyrics'),






]
