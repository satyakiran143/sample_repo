from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    sno=models.IntegerField()
    email=models.EmailField()
    phn=models.IntegerField()
    addr=models.CharField(max_length=40)
    com=models.CharField(max_length=20)
    skills=models.CharField(max_length=40)
