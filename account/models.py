from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



# # Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=60)
    caption = models.TextField()
   

class profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile/')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete = models.CASCADE)

class Like(models.Model):
    like = models.BooleanField()
    image = models.ForeignKey(Image, on_delete = models.CASCADE,related_name='imagelikes')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='userlikes')

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')

class Follows(models.Model):
    follower = models.ForeignKey(profile, related_name='following',on_delete = models.CASCADE)
    followee = models.ForeignKey(profile, related_name='followers',on_delete = models.CASCADE)
