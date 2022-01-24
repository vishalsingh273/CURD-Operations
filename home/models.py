from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    Roll=models.CharField(max_length=10)
    Name=models.CharField(max_length=20)
    Clas=models.CharField(max_length=20)
    School=models.CharField(max_length=40)
    Mobile=models.IntegerField()
    Address=models.CharField(max_length=100)

class StudentAcadmics(models.Model):
    Roll_no=models.CharField(max_length=10)
    Maths=models.CharField(max_length=10)
    Physics=models.CharField(max_length=10)
    Chemistry=models.CharField(max_length=10)
    Biology=models.CharField(max_length=10)
    English=models.CharField(max_length=10)
