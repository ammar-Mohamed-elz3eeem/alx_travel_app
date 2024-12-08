from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=False)
    location = models.CharField(max_length=255, blank=False)
    price_per_night = models.DecimalField(blank=False, null=False, decimal_places=3, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
