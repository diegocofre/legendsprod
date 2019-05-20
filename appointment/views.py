from django.shortcuts import render
from django.contrib import admin
from . import models
from datetime import datetime

# Create your views here.

def index(request):
    authorized_email = "diego.cofre@gmail.com"

    # TODO: Autenticar
    usr = models.User.objects.filter(email__exact=authorized_email).first(); 

    if (not usr):
        error = {
            'msg' : "User is unregistered. Please register here",
        }

        return render(request, 'error.html', context = error)
    else:  
        appolist = models.Appointment.objects.filter(taker_user__exact=usr, status= 'P', starting_at__gt = datetime.now()).order_by('starting_at')      
        context = {
            'usr' : usr,
            'totalappointments' : appolist.count(),
            'appointments' : appolist
        }
        
        return render(request, 'index.html', context = context)



