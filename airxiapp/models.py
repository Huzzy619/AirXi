from django.db import models
from .helpers import get_media_paths
# Create your models here.

class Airport(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Taxi(models.Model):

    TYPES = (
        ('SUV', 'SUV'),
        ('Limousine', 'Limousine'),
        ('Hybrid','Hybrid'),
        ('Cab','Cab')
    )

    Type = models.CharField(max_length=225, choices=TYPES)
    model = models.CharField(max_length=255)
    image = models.ImageField(upload_to = get_media_paths, null= True, blank=True ) 



class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING)
    passengers = models.PositiveSmallIntegerField()
    drop_off_address = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    reference_number = models.CharField(max_length=20, editable=False)

    def __str__(self) -> str:
        return f'{self.name}-{self.reference_number}'

class Contact (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=14)
    subject = models.CharField(max_length=255)
    date_created= models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ['name', 'email', 'subject'] 

class Newsletter(models.Model):
    email = models.EmailField(unique=True)