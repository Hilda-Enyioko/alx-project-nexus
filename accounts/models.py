from django.db import models
from django.contrib.auth.models import AbstractUser

# User profile for policy-holders and admins
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'ADMIN'),
        ('user', 'USER')
    ]
    role = models.TextField(choices=ROLE_CHOICES)
    
    def __str__(self):
        return self.user.username
    