from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            userName=user.username,
            email=user.email,
            name=user.first_name,
        )
        print(profile)


post_save.connect(createProfile, sender=User)