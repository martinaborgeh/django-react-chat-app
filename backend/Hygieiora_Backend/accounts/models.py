from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
import uuid

from .choices import CHOICES, CONDITION
from .validators import CustomEmailValidator
from .helper_model import BaseModel


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)

        validators = [CustomEmailValidator(domain="st.knust.edu.gh")] if role == "patient" else []

        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)

        user._password = None 
        user.full_clean()

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, role=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        validators = [CustomEmailValidator(domain="st.knust.edu.gh")] if role == "patient" else []

        return self.create_user(email, password, role=role, **extra_fields)
        


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    role = models.CharField(
        max_length=10, choices=[("patient", "Patient"), ("doctor", "Doctor")]
    )
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "role"]

    def __str__(self):
        return f"{self.email}"


class Patient(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    condition = models.CharField(choices=CONDITION, max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.user.email} | {self.user.full_name}"


class Doctor(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(choices=CHOICES, max_length=256)
    availability = models.TimeField(default="09:00")
    location = models.CharField(max_length=256, default="Accra")

    def __str__(self):
        return f"{self.user.email} | {self.user.full_name}"
