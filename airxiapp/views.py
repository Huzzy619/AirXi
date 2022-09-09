from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView

from airxiapp.forms import BookingForm, ContactForm

from .models import Airport, Taxi, Newsletter

# Create your views here.
    

class index (TemplateView):
    template_name = 'airxiapp/index.html'

class about(TemplateView):
    template_name = 'airxiapp/about.html'

def contact(request):
    if request.method == 'POST':

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            name = contact_form.cleaned_data.get('name')
            messages.success(
                request, f"{name}, Your message has been sent successfully")
            return redirect('index')
            # messages.info(request, "You have already left a message")
        else:
            messages.error(request, "invalid inputs")

    contact_form = ContactForm()
    context = {"form": contact_form}

    return render(request, 'airxiapp/contact.html', context)


def make_booking(request):

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()
            print(booking_form.cleaned_data.get('taxi'))
            messages.success(
                request, "Your booking has been made successfully")
            return redirect('/')

        else:
            print("Didn't work")
            messages.error("Invalid inputs")

    booking_form = BookingForm()
    airports = Airport.objects.all()

    context = {
        "airports": airports,
        "booking_form": booking_form
    }

    return render(request, 'airxiapp/ride.html', context)



# This View helps make the car list dynamic on ride.html
def model(request):
    from airxiapp.models import Taxi
    Type = request.GET.get('Type')
    models = Taxi.objects.filter(Type=Type)
    all_models = Taxi.objects.all()

    context = {
        'all': all_models,
        'models': models,
    }

    return render(request, 'airxiapp/extra.html', context)



class Taxi (ListView):
    queryset = Taxi.objects.filter()
    # paginate_by = 4
    template_name = 'airxiapp/test.html'
    context_object_name = 'all_taxis'


def taxi(request):

    context = {
        'all_taxis': Taxi.objects.all(),
        # not perfect yet
        'popular_taxis':  Taxi.objects.filter()

    }

    return render(request, 'airxiapp/taxi.html', context)

def newsletter (request):
    if request.method == 'POST':
        try:

            Newsletter.objects.create(
                email = request.POST['email']
            )
            messages.success(request, "You have successfully Subscribed to AirXi mails")
            return redirect('index')

        except IntegrityError: 
            messages.info(request, "You've already subscribed to Airxi mails")
            return redirect('index')




def test(request):

    from airxiapp.models import Taxi

    Taxi.objects.filter()
    
    return render(request, 'airxiapp/test.html')
