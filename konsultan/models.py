from django.db import models
from users.models import CustomUser, CustomUserProfile

# Create your models here.

class Konsultan(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  user_profile = models.OneToOneField(CustomUserProfile, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  is_approved = models.BooleanField(default=False)

  def __str__(self):
    return self.first_name + " " + self.last_name