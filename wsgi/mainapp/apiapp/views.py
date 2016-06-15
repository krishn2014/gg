from django.http import HttpResponse

# importing models
from models import *


# Django REST framework
from serializers import *
from rest_framework import generics


class GenresList(generics.ListCreateAPIView):
    queryset = Genres.objects.all().order_by('name')
    serializer_class = GenresSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class TracksList(generics.ListCreateAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer 


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer
