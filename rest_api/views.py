from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from airxiapp.models import *
from .serializers import *


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MakeBookingSerializer
        return BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        serializer = BookingSerializer(instance=instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TaxiViewSet(ModelViewSet):

    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer


class ContactViewSet(ModelViewSet):

    http_method_names = ['get', 'post', 'options', 'head']
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class NewsletterViewSet(ModelViewSet):

    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
