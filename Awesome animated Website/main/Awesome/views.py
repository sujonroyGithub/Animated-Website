
from email import message
from re import template
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render 
from datetime import datetime
from Awesome.models import Contact
from django.contrib import messages 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent Successfully.')
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')
                      