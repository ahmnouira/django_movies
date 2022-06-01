from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request: HttpRequest): 
    return render(request, "home.html", {'name': 'Ahmed Nouira'})

def about(request: HttpRequest): 
    return HttpResponse('<h3>Welcome to About Page</h3>')
