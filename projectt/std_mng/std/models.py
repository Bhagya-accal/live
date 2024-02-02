from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    password = models.CharField(max_length=300)
    course = models.CharField(max_length=300)
    images = models.ImageField(upload_to='picture')
    
    def __str__(self):
        return self.name
    