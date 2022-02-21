from django.db import models
from django.core.validators import RegexValidator
import re
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save


class UserManager(models.Manager):
    def validate(self, form):
        errors = {}

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        
        if form['adminKey'] != 'WolvesDragonFlies&Bees':
            errors['adminKey'] = 'Please see webmaster for the admin key'

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)
    adminKey = models.CharField(max_length=255)

    objects = UserManager()

    userCreatedAt = models.DateTimeField(auto_now_add=True)
    userUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=CASCADE)
    image = models.ImageField(upload_to='profileImgs', default='bee.jpg')
    def __str__(self):
        return f'{self.user.firstName} Profile'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)

class Topic(models.Model):
    topic = models.CharField(max_length=255)
    def __str__(self):
        return self.topic

class Genre(models.Model):
    topic = models.OneToOneField(Topic, unique=True, on_delete=CASCADE)
    def __str__(self):
        return f'{self.topic.topic} Genre'

def create_topic_genre(sender, instance, created, **kwargs):
    if created:
        Topic.objects.create(topic=instance)
        post_save.connect(create_topic_genre, sender=Topic)

class Dvd(models.Model):
    title = models.CharField(max_length=255)
    actors = models.TextField(blank=True)
    year = models.CharField(max_length=255, blank=True)
    misc = models.TextField(max_length=255, blank=True)
    user = models.ForeignKey(User, related_name='owner', on_delete=CASCADE)
    genre = models.ForeignKey(Topic, related_name='theTopic', on_delete=CASCADE)

class Movie(models.Model):
    movie = models.OneToOneField(Dvd, unique=True, on_delete=CASCADE)
    img = models.ImageField(upload_to='movieImgs', default='bee.jpg')
    def __str__(self):
        return f'{self.dvd.movie} Movie'

def create_dvd_movie(sender, instance, created, **kwargs):
    if created:
        Dvd.objects.create(dvd=instance)
        post_save.connect(create_dvd_movie, sender=Dvd)

class Cds(models.Model):
    albumTitle = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    year = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, related_name='theOwner', on_delete=CASCADE)

class Music(models.Model):
    music = models.OneToOneField(Cds, unique=True, on_delete=CASCADE)
    img = models.ImageField(upload_to='musicImgs', default='bee.jpg')
    def __str__(self):
        return f'{self.cds.music} Music'

def create_cds_music(sender, instance, created, **kwargs):
    if created:
        Cds.objects.create(cds=instance)
        post_save.connect(create_cds_music, sender=Cds)