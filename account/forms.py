from django import forms
from django.contrib.gis import forms as gisforms
#from .widgets import OpenLayersWidget
from .models import PoliceStation, Hospital, Customer, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')



class PoliceStationForm(forms.ModelForm):
    class Meta:
        model = PoliceStation
        exclude = ['admin'] 
        widgets = {
            'location' : gisforms.OSMWidget(attrs={'map_width': 800, 
                                                   'map_height': 500,
                                                   'default_lon': 76.614787,
                                                   'default_lat': 27.552189,
                                                   'display_raw': True})
        }


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        exclude = ['admin']
        widgets = {
            'location' : gisforms.OSMWidget(attrs={'map_width': 800, 
                                                   'map_height': 500,
                                                   'default_lon': 76.614787,
                                                   'default_lat': 27.552189,
                                                   'display_raw': True})
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']