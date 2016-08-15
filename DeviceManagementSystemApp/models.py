from django.db import models

# Create your models here.


class Students(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=150, blank=True, default='')
    access_token = models.CharField(max_length=50, blank=True, default='')

class Devices(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=150, blank=True, default='')
    owner = models.OneToOneField(Students)
    date_time = models.DateTimeField(blank=False)
    used_for = models.TextField()
    type = models.CharField(max_length=20, blank=True, default='')
    issues = models.TextField()
