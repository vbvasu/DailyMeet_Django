from django.db import models

# Create your models here.
class Demo(models.Model):
    Name = models.CharField(max_length=20)
    age = models.IntegerField()
