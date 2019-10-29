from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Review(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    def __str__(self):
        return self.content