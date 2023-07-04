from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request,"booking/index.html")

def about(request):
    return render(request,'booking/about.html')

def booking(request):
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'booking/confirmation.html')
    form = BookingForm()
    context = {'form' : form}
    return render(request,'booking/booking.html',context)

def doctors(request):
    doctors = Doctors.objects.all()
    context = {'doctors' : doctors}
 
    return render(request,'booking/doctors.html',context)

def department(request):
    dict_dept = Departments.objects.all()

    context = {"dict_dept": dict_dept}

    return render(request,'booking/departments.html',context)

def contact(request):
    return render(request,'booking/contact.html')
