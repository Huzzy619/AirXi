from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Booking, Newsletter



@receiver(post_save, sender = Booking )
def suscribe_to_newsletter (*args, **kwargs):
    if kwargs['created']:

    #The get or create method ensures an email is not duplicated in the database
       newsletter, created =  Newsletter.objects.get_or_create(email = kwargs['instance'].email) 
