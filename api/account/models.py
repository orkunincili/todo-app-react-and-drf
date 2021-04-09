from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.


class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, username, name, password=None):


        if not username:
            raise ValueError('User must have an username')

        

        user = self.model(username=username, name=name)
        user.set_password(password)

        user.save(using=self._db) #specify to database

        return user


    def create_superuser(self, username, name, password,**other_fields):
        """Create and save a new super user with given details"""
        if not username:
            raise ValueError('Superuser must have an username')

        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        user = self.create_user(username, name, password)

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Retrieve full name of user"""

        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""

        return self.name

    def __str__(self):
        """Return string representation of our user"""

        return self.username
