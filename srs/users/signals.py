from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.models import Profile, Location

# Create a signal to get the data from user and instance create new user in profile section
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Create a signal to get the data from user and instance create new location in profile section
@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created, **kwargs):
    if created:
        profile_location = Location.objects.create()
        instance.location = profile_location
        instance.save()

# Delete a user location
@receiver(post_delete, sender=Profile)
def delete_profile_location(sender, instance, *args, **kwatgs):
    if instance.location:
        instance.location.delete()