from django import forms
from django.forms import ModelForm
from .models import *


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input a name of venue'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input zip code'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input  phone number'}),
            'web_address': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Input web address'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Input E-mail address'}),
        }
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone_number': '',
            'web_address': '',
            'email_address': ''
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input a name of event'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input date'}),
            'event_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input time'}),
            'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select venue'}),
            'manager': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Select attendees'}),
        }
        labels = {
            'name': '',
            'event_date': '',
            'event_time': '',
            'venue': '',
            'manager': '',
            'attendees': ''
        }
