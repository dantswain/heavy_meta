"""
Model definitions
"""

from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    """
    Represents a song - a collection of tracks
    """
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField(blank=True, null=True)


class Track(models.Model):
    """
    Represents a recording track
    """
    title = models.CharField(max_length=200)
    song_order = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)


class Take(models.Model):
    """
    Represents a recording track
    """
    title = models.CharField(max_length=200)
    track_order = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)


class TakeComment(models.Model):
    """
    Represents user discussion around a take
    """
    take = models.ForeignKey(Take, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
