from django.db import models
from django.contrib.gis.db import models as geomodels
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_hospital_admin = models.BooleanField(default=False)
    is_police_station_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    rel_phone = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=30, unique=True)
    blood_group = models.CharField(max_length=5, null=True, blank=True)


class PoliceStation(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, related_name='police_station')
    name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True)
    location = geomodels.PointField()

    def __str__(self):
        return self.name


class Hospital(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hospital')
    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True)
    location = geomodels.PointField()

    def __str__(self):
        return self.name


