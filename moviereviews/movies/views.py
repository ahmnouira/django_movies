from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request: HttpRequest): 
    return render(request, "home.html")

def about(request: HttpRequest): 
    return render(request, "about.html", {'name': "Ahmed Nouira", 'page_name': "About"})

def contact(request: HttpRequest): 
        return HttpResponse('<h3 style="color:green;">Welcome to Contact Page</h3>')
