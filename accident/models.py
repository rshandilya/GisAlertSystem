from django.db import models
from django.conf import settings
from account.models import Customer, Hospital, PoliceStation
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

# Create your models here.

class Accident(models.Model):

    STATUS = [
        ('DET', 'Detect'),
        ('ACK', 'Acknowledge'),
        ('CNF', 'Confirm'),
    ]

    lat = models.DecimalField(decimal_places=7, max_digits=9)
    lon = models.DecimalField(decimal_places=7, max_digits=9)
    occurrence = models.DateTimeField(auto_now_add=True)
    vehicle = models.CharField(max_length=30)
    status = models.CharField(max_length=5, choices=STATUS, default='DET')

    def get_customer(self):
        try:
            cutomer = Customer.objects.get(vehicle_no=self.vehicle)
        except Customer.DoesNotExist:
            return None
        return cutomer.id
        
    def get_nearest_hospital(self):
        ac_pnt = Point(float(self.lon), float(self.lat), srid=4326)
        hospitals = Hospital.objects.annotate(dist=Distance('location', ac_pnt)).order_by('dist')
        return hospitals[0]

    
    def get_nearest_police_station(self):
        ac_pnt = Point(self.lon, self.lat, srid=4326)
        ps = PoliceStation.objects.annotate(dist=Distance('location', ac_pnt)).order_by('dist')
        return ps[0]
       
    

