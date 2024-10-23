# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # All necessary fields are already included in AbstractUser, such as:
    # first_name, last_name, username, email, and password.
    
    # If you want to add extra fields, you can define them here:
    # phone = models.CharField(max_length=15, null=True, blank=True)  # Example custom field
    
    pass

    def __str__(self):
        return self.username  # Or return email or other field, based on preference
