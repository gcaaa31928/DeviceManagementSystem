from django.db import models

# Create your models here.


class Students(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=150, blank=True, default='')
    access_token = models.CharField(max_length=50, blank=True, null=True)
    manager = models.BooleanField(default=False)
    mail = models.EmailField(null=True)

class Devices(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=150, blank=True, default='')
    owner = models.OneToOneField(Students,null=True)
    check_in_date_time = models.DateTimeField(blank=True, null=True)
    used_for = models.TextField(null=True)
    type = models.CharField(max_length=20, blank=True, default='')
    issues = models.TextField(null=True)
    property_number = models.IntegerField(default=0)
    token = models.CharField(max_length=50, blank=True, default='', null=True)
