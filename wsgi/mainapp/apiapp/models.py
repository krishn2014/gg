# defining models here

from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Tracks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=200)
    genres = models.ManyToManyField('Genres')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.title.strip() == '':
            raise ValidationError("'title' field cannot be empty") 

    class Meta:
        managed = True
        db_table = 'tracks'


class Genres(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    class Meta:
        managed = True
        db_table = 'genres'