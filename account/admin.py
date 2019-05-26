from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import PoliceStation, Hospital, User, Customer
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = settings.AUTH_USER_MODEL
    list_display = ['email', 'username',]
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Permissions', {'fields': ('is_hospital_admin', 'is_police_station_admin'),
               }),
    ) 

admin.site.register(User, CustomUserAdmin)



class PoliceStationAdmin(OSMGeoAdmin):
    default_lat = 27.552189
    default_lon = 76.614787
    
admin.site.register(PoliceStation, PoliceStationAdmin)


class HospitalAdmin(OSMGeoAdmin):
    default_lat = 27.552189
    default_lon = 76.614787

admin.site.register(Hospital, HospitalAdmin)

admin.site.register(Customer)