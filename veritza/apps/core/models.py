from django.db import models
from django.contrib.auth.models import AbstractUser

from django_extensions.db.fields import UUIDField

class User(AbstractUser):
    uuid = UUIDField()



class DummyProfile(models.Model):
    pass


class Dataset(models.Model):
    pass