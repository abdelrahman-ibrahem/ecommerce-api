# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE = (
    ('admin', 'admin'),
    ('normal', 'normal'),
)

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profile", null=True, blank=True)
    phone = models.CharField(max_length=11)
    role = models.CharField(max_length=255, choices=ROLE, default='normal')