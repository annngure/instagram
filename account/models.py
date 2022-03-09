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
   

# class profile(models.Model):
#     name = models.CharField(max_lenght =60)
#     bio = models.TextField()

