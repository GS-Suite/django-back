from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.db import models

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    username = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100, blank = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(auto_now = True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.name


# Create your models here.


