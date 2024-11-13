from django.shortcuts import render, redirect
from myapp.models import Appointment, Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request,'service-details.html')

def starters(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    return render(request, 'doctors.html')

def myservice(request):
    return render(request, 'services.html')

def appointments(request):
    if request.method == 'POST':
        myappointment=Appointment(
            name =request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            datetime = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )

        myappointment.save()
        return redirect('/appointments')
    else:
        return render(request,'appointments.html')

def contact(request):
    if request.method == 'POST':
        mycontact=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message = request.POST['message']
        )

        mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')
