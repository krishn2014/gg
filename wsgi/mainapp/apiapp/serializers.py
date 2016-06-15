from rest_framework import serializers

# importing models
from models import *
from django.core.exceptions import ValidationError


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id', 'name']
        read_only_fields = ('id',)


class TracksSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField( many=True, slug_field='name')


    def validate(self, data):
        """
        Check that the title should not change in update
        """
        if self.data['title'] != '' and self.data['title'] != data['title']:
            raise serializers.ValidationError("'title' field cannot be updated")
        return data

    class Meta:
        model = Tracks
        fields = ('id', 'title', 'genres', 'rating')
        read_only_fields = ('id',)

