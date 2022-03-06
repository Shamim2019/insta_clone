from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import UserManager
# Create your models here.
class user(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures'null = False)

    # USERNAME_FIELD ='username'
    # EQUIRED_FIELDS = []

    # objects=BaseuserManager()
 