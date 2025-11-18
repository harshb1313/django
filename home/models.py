from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    phoneNumber = models.CharField(max_length=10, blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)
