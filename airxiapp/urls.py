from django.urls import path, include
from .views import *



urlpatterns = [

    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('ride', make_booking, name='make_booking'),
    path('taxi', taxi, name='taxi'),
    path('model', model, name='model'),
    path('test', test)


]
