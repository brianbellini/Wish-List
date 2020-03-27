from django.db import models
from django.urls import reverse


# Create your models here.
class Wish(models.Model):
  description = models.CharField(max_length= 50)

  def __str__(self):
    return self.description