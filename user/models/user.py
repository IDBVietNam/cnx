from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, c_username, c_email, c_password=None, **extra_fields):
        if not c_email:
            raise ValueError("Email is required")
        if not c_username:
            raise ValueError("Username is required")

        email = self.normalize_email(c_email)
        user = self.model(c_username=c_username, c_email=email, **extra_fields)
        user.set_password(c_password)
        user.save(using=self._db)
        return user

    def create_superuser(self, c_username, c_email, c_password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(c_username, c_email, c_password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    c_username = models.CharField(max_length=150, unique=True)
    c_email = models.EmailField(unique=True)
    c_firstName = models.CharField(max_length=50)
    c_lastName = models.CharField(max_length=50)
    c_password = models.CharField(max_length=128)  # Django handles password hashing
    c_status = models.BooleanField(default=True)
    c_userRoles = models.CharField(max_length=50, default="user")

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "c_username"
    REQUIRED_FIELDS = ["c_email", "c_firstName", "c_lastName"]

    def __str__(self):
        return self.c_username
