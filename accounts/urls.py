from django.urls import path
from .views import sign_out, sign_up, sign_in

urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("logout/", sign_out, name="logout"),
    path("login/", sign_in, name="login")
]