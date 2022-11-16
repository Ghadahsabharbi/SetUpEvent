from django.db import models


# Create your models here.
class Event(models.Model):
    idea_owner=models.CharField(max_length=300)
    sponser=models.CharField(max_length=300)
    autherity=models.CharField(max_length=300)
    name=models.CharField(max_length=300)
    date= models.DateTimeField()
    place=models.CharField(max_length=300)
    city=models.CharField(max_length=300)
    status=models.CharField(max_length=300)
    description= models.TextField()