from django.db import models

# Create your models here.

class Hospital(models.Model):
    sido = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    medical = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    tel = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    

