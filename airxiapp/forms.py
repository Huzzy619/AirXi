from django import forms
from .models import Booking, Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'phone', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'type':'email'}),
            'message': forms.TextInput(attrs={'placeholder': 'Enter a message here'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),

        }


class BookingForm (forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'airport',
                  'passengers', 'drop_off_address', 'date', 'time', 'taxi']
        exclude = ['reference_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'type':'email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'passengers': forms.TextInput(attrs={'placeholder': 'Passenger(s)', 'type':'number'}),
            'drop_off_address': forms.TextInput(attrs={'placeholder': 'Enter Drop off Address'}),
            'date':  forms.TextInput(attrs={'placeholder': 'date', 'type': 'date'}),
            'time':  forms.TextInput(attrs={'placeholder': 'time', 'type': 'time'})



        }
