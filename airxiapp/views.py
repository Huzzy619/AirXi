from django.shortcuts import render
from django.contrib.messages import success, warning
from airxiapp.forms import ContactForm
from django.http import JsonResponse
from .models import Airport, Booking, Taxi
from asgiref.sync import sync_to_async
from django.core.serializers import serialize

# Create your views here.


def index(request):
    return render(request, 'airxiapp/index.html')


def about(request):
    return render(request, 'airxiapp/about.html')


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            success(request, "Your message has been sent successfully")
            return JsonResponse({"status": "Your message has been sent successfully"})
        else:
            warning(request, "message not sent")
            print("Not Sent")
    return render(request, 'airxiapp/contact.html')


def default(request):
    return render(request, 'airxiapp/404.html')


def ride(request):

    context =  {

        "airports": Airport.objects.all()
    }


    return render(request, 'airxiapp/ride.html', context)


def model(request):
    Type = request.GET.get('Type')
    models = Taxi.objects.filter(Type=Type)
    all_models = Taxi.objects.all()

    context = {
        'all': all_models,
        'models':models,
    }

    return render(request, 'airxiapp/extra.html', context)
    


def taxi(request):

    return render(request, 'airxiapp/taxi.html')


def newsletter(request):
    if request.method == 'POST':
        
        pass
    return success(request, "You've been added to our mailing list")
