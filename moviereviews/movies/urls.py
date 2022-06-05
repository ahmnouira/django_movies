from django.urls import path
from .views import details

urlpatterns  = [
        path('<int:movie_id>', details, name='details')
]