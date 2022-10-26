from ast import Mod
import code
from email.mime import image
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=255)

class Offer(models.Model):
    code = models.CharField(max_length=16)
    discription = models.CharField(max_length=255)
    discount = models.FloatField()

