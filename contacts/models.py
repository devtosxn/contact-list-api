from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=30)
    avatar = models.URLField(null=True, blank=True)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
