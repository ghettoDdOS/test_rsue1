from django.db import models


# Create your models here.
class Person(models.Model):
    full_name = models.CharField(max_length=256)
    corp = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    mail = models.CharField(max_length=256)
