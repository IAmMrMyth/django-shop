from django.db import models

# Create your models here.


class Color(models.Model):
    title = models.CharField(max_length=64)
    color_code = models.CharField(max_length=16)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
