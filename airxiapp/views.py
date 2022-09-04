import email
from re import sub
from django.shortcuts import render, redirect
from django.contrib import messages 
from airxiapp.forms import BookingForm, ContactForm
from django.http import JsonResponse, Http404
from .models import Airport, Booking, Contact, Taxi
from asgiref.sync import sync_to_async
from django.core.serializers import serialize
from django.db import IntegrityError


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
                name  = contact_form.cleaned_data.get('name')
                messages.success(request, f"{name}, Your message has been sent successfully")
                return redirect('index')
                # messages.info(request, "You have already left a message")
        else:
            messages.error(request, "invalid inputs")
            
    contact_form = ContactForm()
    context = {"form":contact_form}

    return render(request, 'airxiapp/contact.html', context)


def make_booking(request):
    
    
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()
            print(booking_form.cleaned_data.get('taxi'))
            messages.success(request, "Your booking has been made successfully")
            return redirect ('/')
        
        else:
            print("Didn't work")
            messages.error("Invalid inputs")



    booking_form = BookingForm()
    airports = Airport.objects.all()

    context = {
        "airports":airports,
        "booking_form": booking_form
    }



   
    return render(request, 'airxiapp/ride.html', context)


def model(request):
    Type = request.GET.get('Type')
    models = Taxi.objects.filter(Type=Type)
    all_models = Taxi.objects.all()

    context = {
        'all': all_models,
        'models': models,
    }

    return render(request, 'airxiapp/extra.html', context)


def taxi(request):
    
    context = {
    'all_taxis' : Taxi.objects.all(),
    'popular_taxis' :  Taxi.objects.order_by('-bookings').filter(bookings__gt = 20).distinct()[:4] #not perfect yet

    }
    return render(request, 'airxiapp/taxi.html', context)


def newsletter(request):
    if request.method == 'POST':

        pass
    return messages.success(request, "You've been added to our mailing list")


def test(request):
    from .forms import BookingForm, ContactForm

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request)
            print("saved successfully")
            return redirect('/')
        else:
            print(" It did not Work")
        
    return render(request, 'airxiapp/test.html', {"form": form})



