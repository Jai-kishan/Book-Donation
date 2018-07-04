
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Personal_details(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    username =models.CharField(max_length=200)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    state =models.CharField(max_length=200)
    country =models.CharField(max_length=200)
    contact_number =models.CharField(max_length=200)
    

class Book(models.Model):
    book_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book_author =models.CharField(max_length=200)
    book_title = models.CharField(max_length=200)
    book_discription = models.TextField()
    book_photo=models.ImageField(blank=True, null=True)
    Personal_details = models.ForeignKey('Personal_details')

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()