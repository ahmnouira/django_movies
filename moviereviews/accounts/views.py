from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.

def _response(request: HttpRequest, error = None): 
        return render(request, 'signup.html', {
            'form': UserCreationForm, 
            'error': error
        })

def signup(request: HttpRequest): 
    if request.method == "GET": 
       return _response(request=request)
    else: 
        password1 = request.POST["password1"] 
        password2 = request.POST["password2"]

        if password1 == password2: 
            # check password length is less than eight
            if len(password1) < 8: 
              return _response(request, error='Weak password')
            username  = request.POST['username']
            try: 
                user  = User.objects.create_user(username, password1)
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
               return _response(request, error="Username already taken. Choose new username")
        else: 
           return _response(request, error="Passwords do not match")








