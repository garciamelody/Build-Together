from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 



class Room(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length =30)
    #null = True allows this field to be blank
    description = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    #takes a snapshot every time we save/update the room
    updated = models.DateTimeField(auto_now = True)
    #only takes a snapshot the first time the room is created
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        #orders the newest as first (descending order)
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    #CASCADE means that all messages will get deleted
    room = models.ForeignKey(Room, on_delete = models.CASCADE) 
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        #returns the first 50 chars
        return self.body[0:50]
        