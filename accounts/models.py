from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .validators import phone_number_validator
# Create your models here.

# TODO: complate user model
class User(AbstractBaseUser,PermissionsMixin):
    phone_number = models.CharField(max_length=11,validators=[phone_number_validator])
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "phone_number" 
    
    def __str__(self):
        return self.phone_number
# TODO: write profile model 
class Profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user.phone_number}"
