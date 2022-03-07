from django.db import models


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    caption = models.TextField()
     
class profile(models.Model):
    name = models.CharField(max_lenght =60)
    bio = models.TextField()

class likes(models.Model):
    like = models.BooleanField()

class comment(models.Model):
    comment=models.TextField()

class Follows(models.Model):
    follower
    followee
     