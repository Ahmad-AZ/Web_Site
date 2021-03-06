from django.db import models


class Album(models.Model):  # a blueprint how that going to store in the database
    artist = models.CharField(max_length=250)  # those are the fields will create in the database
    album_title = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=1000)

    def __str__(self): # string representation of this object
        return self.artist +" - "+ self.album_title





class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
