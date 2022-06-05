from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.

def signup(request: HttpRequest): 

    if request.method == "GET": 
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else: 
        password1 = request.POST["password1"] 
        password2 = request.POST["password2"]
        if password1 == password2: 
            username  = request.POST['username']
            user  = User.objects.create_user(username, password1)
            user.save()
            login(request, user)
            return redirect('home')
        else: 
            return render(request, 'signup.html', {
                'form': UserCreationForm, 'error': 'Passwords do not match'
            })






