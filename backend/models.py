from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Post(models.Model):
    nomi = models.CharField(max_length=20)
    rasm = models.ImageField(upload_to = "rasmlar/")

    def __str__(self):
        return self.nomi