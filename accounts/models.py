from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    bio = models.CharField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='user_profile')

    def __str__(self):
        return self.bio
    
class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    current = models.BooleanField()
    description = models.TextField()

class Experience(models.Model):
    job = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    start = models.DateTimeField()
    end = models.DateTimeField()
    current = models.BooleanField()
    description = models.TextField()
