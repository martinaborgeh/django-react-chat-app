from django.db import models

from .choices import GENDER


class BaseModel(models.Model):
    gender = models.CharField(choices=GENDER, max_length=256)
