from django.urls import path, include
from .views import *


urlpatterns = [
    
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('default', default, name= '404'),
    path('ride', ride, name= 'ride'),
    path('taxi', taxi, name= 'taxi'),
    path('model', model, name='model')


]
