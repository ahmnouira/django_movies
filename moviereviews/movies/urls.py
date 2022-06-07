from django.urls import path
from .views import details, add_review

urlpatterns = [
    path('<int:movie_id>', details, name='details'),
    path('<int:movie_id>/add-review', add_review, name='add-review')
]
