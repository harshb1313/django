from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    phoneNumber = models.CharField(max_length=10, blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)

class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
