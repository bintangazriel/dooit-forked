from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.
class CustomUserManager(BaseUserManager):
  def create_user(self, company_name, username, email, password=None):
    if not email:
      raise ValueError('User must have an email address')

    if not username:
      raise ValueError('User must have an username')

    user = self.model(
      email = self.normalize_email(email),
      username = username,
      company_name = company_name
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, company_name, username, email, password=None):
    user = self.create_user(
      email = self.normalize_email(email),
      username = username,
      password = password,
      company_name= company_name
    )
    user.is_admin = True
    user.is_active = True
    user.is_staff = True
    user.is_superadmin = True
    user.save(using=self._db)
    return user


class CustomUser(AbstractBaseUser):
  PENCATAT = 1
  KONSULTAN = 2

  ROLE_CHOICE = (
    (PENCATAT, 'Pencatat'),
    (KONSULTAN, 'Konsultan'),
  )

  company_name = models.CharField(max_length=50)
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=100, unique=True)
  role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

  # required fields
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now_add=True)
  created_date = models.DateTimeField(auto_now_add=True)
  modified_date = models.DateTimeField(auto_now=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_superadmin = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'company_name']

  objects = CustomUserManager()

  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return self.is_admin

  def has_module_perms(self, app_label):
    return True

  def get_role(self):
    if self.role == 1:
      user_role = 'Pencatat'
    elif self.role == 2:
      user_role = 'Konsultan'
    return user_role


class CustomUserProfile(models.Model):
  user = OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
  company_prof_pic = models.ImageField(upload_to='profile_pic', blank=True, null=True, default='profile_pic/default.png')
  company_bio = models.CharField(max_length=100, blank=True, null=True)

  def __str__(self):
    return self.user.email

  def save(self, *args, **kwargs):
    return super(CustomUserProfile, self).save(*args, **kwargs)