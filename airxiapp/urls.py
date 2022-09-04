from django.urls import path
from airxiapp.views import *



urlpatterns = [

    path('', index.as_view(), name='index'),
    path('about', about.as_view(), name='about'),
    path('contact', contact, name='contact'),
    path('ride', make_booking, name='make_booking'),
    path('taxi', taxi, name='taxi'),
    path('model', model, name='model'),
    path('newsletter', newsletter, name = 'newsletter'),
    path('test', Taxi.as_view())


]
