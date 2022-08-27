from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=50)
    img = models.ImageField(upload_to='iventory/product')

    def __str__(self):
        return self.name