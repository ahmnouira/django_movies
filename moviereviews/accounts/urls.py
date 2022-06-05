from django.urls import path
from .views import sign_out, signup

urlpatterns  = [
    path("signup/", signup, name="signup"), 
    path("logout", sign_out, name="logout")
]