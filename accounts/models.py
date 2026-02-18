from django.db import models
from django.contrib.auth.models import AbstractUser

# User profile for policy-holders and admins
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'ADMIN'),
        ('user', 'USER')
    ]
    role = models.TextField(choices=ROLE_CHOICES)
    
    # Use Email for Login Authentication inline with JWT authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] #username is still a required field
    
    def __str__(self):
        return self.email
    