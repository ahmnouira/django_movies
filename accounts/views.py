from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm

# Create your views here.


def _response(request: HttpRequest, error=None):
    return render(request, 'signup.html', {
        'form': UserCreateForm,
        'error': error
    })


def sign_up(request: HttpRequest):
    if request.method == "GET":
        return _response(request=request)
    else:
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            # check password length is less than eight
            if len(password1) < 8:
                return _response(request, error='Weak password')
            username = request.POST['username']
            try:
                user = User.objects.create_user(username, password1)
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return _response(
                    request,
                    error="Username already taken. Choose new username")
        else:
            return _response(request, error="Passwords do not match")


def sign_in(request: HttpResponse):
    if request.method == "GET":
        return render(request, 'login.html', {'form': AuthenticationForm})

    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request=request,
                            username=username,
                            password=password)
        if user is None:
            return render(
                request, "login.html", {
                    'form': AuthenticationForm,
                    'error': "username and password do not match"
                })
        else:
            login(request, user)
            return redirect('home')


@login_required
def sign_out(request: HttpRequest):
    logout(request)
    return redirect('home')
