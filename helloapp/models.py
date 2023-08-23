from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  age = models.IntegerField()


# Create your models here.
  def __str__(self):
    return f"{self.firstname} {self.lastname} {self.city} {self.age} "