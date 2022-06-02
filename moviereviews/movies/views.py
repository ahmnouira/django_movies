from turtle import title
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.

def home(request: HttpRequest): 
    searchTerm = request.GET.get('s')
    print("term:", searchTerm)
    if searchTerm: 
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else: 
        movies  = Movie.objects.all()
    return render(request, "home.html", {'term': searchTerm, 'movies': movies})

def about(request: HttpRequest): 
    return render(request, "about.html", {'name': "Ahmed Nouira", 'page_name': "About"})

def contact(request: HttpRequest): 
        return HttpResponse('<h3 style="color:green;">Welcome to Contact Page</h3>')


def signup(request: HttpRequest):
    email = request.GET.get('email')
    return render(request, "signup.html", {'email': email}) 


    
