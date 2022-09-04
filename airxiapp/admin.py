from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Airport)
class AiportAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    

@admin.register(Taxi)
class TaxiAdmin(admin.ModelAdmin):
    list_display = ['Type', 'model', 'taxi_picture']
    list_per_page = 5
    search_fields = ['Type', 'model']

    def taxi_picture(self, instance):
        if instance.image:
            # url = reverse('admin:airxiapp_taxi_change', args=(instance.id,))
            return format_html(f"<a href='{instance.image.url}'><img src='{instance.image.url}' class='thumbnail'></a>")
        return '-'


    class Media:
        css = {
            'all': ['thumbnail/image.css']
        }
        

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ['name', 'drop_off_address','date','time']
    list_per_page = 10


admin.site.register([Contact,Newsletter])

