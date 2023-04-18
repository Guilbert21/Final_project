from django import forms
from django_google_maps.widgets import GoogleMapsAddressWidget
from .models import TaxiBooking

class TaxiBookingForm(forms.Form):
    class Meta:
        model = TaxiBooking
        fields = ('phone', 'pickup', 'destination', 'time', 'message')
        widgets = {
            'pick_up_location': GoogleMapsAddressWidget(attrs={
                'data-autocomplete-options': {'types': ["geocode"],
                                                'componentRestrictions': {'country': 'mu'}
                                                }
            }),
            'drop_off_location': GoogleMapsAddressWidget(attrs={
                'data-autocomplete-options': {'types': ["geocode"],
                                                'componentRestrictions': {'country': 'mu'}
                }
            }),
        }