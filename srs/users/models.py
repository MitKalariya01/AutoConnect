
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
    
from users.utils import user_directory_path

# Create a model for getting data for location
class Location(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6)
    
    def __str__(self):
        return f'Location {self.id} {self.city}'
    
# Create a model for storing data in profile section
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null=True)
    bio = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Profile {self.user.username}'