from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=75)
    email = models.EmailField(_('Email address'), unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateTimeField(auto_now_add=False)
    is_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, default=None)
    birth_date = models.DateField(null=True, default=None)
    nationality = models.CharField(max_length=80, null=True, blank=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email