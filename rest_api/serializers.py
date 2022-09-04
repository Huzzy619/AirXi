from rest_framework import serializers
from airxiapp.models import *
from airxiapp.helpers import reference_number_generator


class MakeBookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'airport',
                  'passengers', 'drop_off_address', 'date', 'time']

    def save(self, **kwargs):
        new_reference_number = reference_number_generator()

        # Making sure the reference number is unique
        while Booking.objects.filter(reference_number=new_reference_number).exists():
            new_reference_number = reference_number_generator()

        if Booking.objects.filter(**self.validated_data):

            raise serializers.ValidationError(
                "{'error':'The Booking has already been made'}")

        self.instance = Booking.objects.create(
            reference_number=new_reference_number,
            **self.validated_data
        )
        return self.instance


class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'reference_number', 'name', 'email', 'phone',
                  'airport', 'passengers', 'drop_off_address', 'date', 'time']


class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ['Type', 'model', 'image']


class ContactSerializer (serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone',
                  'subject', 'message', 'date_created']


class NewsletterSerializer (serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'email']
