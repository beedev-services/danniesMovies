from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Topic)
def createGenre(sender, instance, created, **kwargs):
    if created:
        Genre.objects.create(topic=instance)

@receiver(post_save, sender=Topic)
def saveGenre(sender, instance, **kwargs):
    instance.genre.save()

@receiver(post_save, sender=Dvd)
def createMovie(sender, instance, created, **kwargs):
    if created:
        Movie.objects.create(movie=instance)

@receiver(post_save, sender=Dvd)
def saveMovie(sender, instance, **kwargs):
    instance.movie.save()

@receiver(post_save, sender=Cds)
def createMusic(sender, instance, created, **kwargs):
    if created:
        Music.objects.create(music=instance)

@receiver(post_save, sender=Cds)
def saveMusic(sender, instance, **kwargs):
    instance.movie.save()