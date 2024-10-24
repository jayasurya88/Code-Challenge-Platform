# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
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
        

# models.py
from django.db import models

class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    input_format = models.TextField()
    output_format = models.TextField()
    examples = models.TextField()

    def __str__(self):
        return self.title




