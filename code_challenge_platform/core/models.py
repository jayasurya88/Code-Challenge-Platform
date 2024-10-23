# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
     GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

     profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
     location = models.CharField(max_length=100, null=True, blank=True)
     birthday = models.DateField(blank=True, null=True)  
     skills = models.TextField(null=True, blank=True)  # Can store as a comma-separated list of skills

     def __str__(self):
        return self.username  
        
