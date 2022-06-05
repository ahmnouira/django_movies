from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request: HttpRequest): 

    return render(request, 'signup.html', {
        'form': UserCreationForm
    })

