from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CategoryMovie(models.Model):
    name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.URLField()
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=255)
    category = models.ManyToManyField(CategoryMovie)
    youtube_trailer_link = models.URLField()
    image = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='pics', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

