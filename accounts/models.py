from django.db import models
from django.contrib.auth.models import User

# User profile for policy-holders and admins
class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'ADMIN'),
        ('user', 'USER')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.TextField(choices=ROLE_CHOICES)
    
    def __str__(self):
        return self.user.username
    