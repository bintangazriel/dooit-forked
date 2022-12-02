from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import CustomUser, CustomUserProfile


@receiver(post_save, sender=CustomUser)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
  if created:
    CustomUserProfile.objects.create(user=instance)
  else:
    try:
      # Update the user profile if it's already exist
      profile = CustomUserProfile.objects.get(user=instance)
      profile.save()
    except:
      # Create the user profile if not exist
      CustomUserProfile.objects.create(user=instance)


@receiver(pre_save, sender=CustomUser)
def pre_save_profile_receiver(sender, instance, **kwargs):
  pass