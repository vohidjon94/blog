from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Category(models.Model):
    nomi = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nomi

class Post(models.Model):
    tanlov = models.ForeignKey(Category, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=20)
    rasm = models.ImageField(upload_to = "rasmlar/")

    def __str__(self):
        return self.nomi