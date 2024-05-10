from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra):
        if not email:
            raise ValueError("Cannot create a user with no email.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra):
        extra.setdefault("is_staff", False)
        extra.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra)

    def get_by_natural_key(self, username):
        return self.get(email__iexact=username)


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
