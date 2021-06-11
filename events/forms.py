from django.forms import ModelForm
from .models import *


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
