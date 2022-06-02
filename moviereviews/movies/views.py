from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request: HttpRequest): 
    term = request.GET.get('searchMovie')
    print(term)
    return render(request, "home.html", {'term': term})

def about(request: HttpRequest): 
    return render(request, "about.html", {'name': "Ahmed Nouira", 'page_name': "About"})

def contact(request: HttpRequest): 
        return HttpResponse('<h3 style="color:green;">Welcome to Contact Page</h3>')


def signup(request: HttpRequest):
    email = request.GET.get('email')
    return render(request, "signup.html", {'email': email}) 


    
