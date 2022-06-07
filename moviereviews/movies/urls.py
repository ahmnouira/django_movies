from django.urls import path
from .views import details, add_review, delete_review

urlpatterns = [
    path('<int:movie_id>', details, name='details'),
    path('<int:movie_id>/add-review', add_review, name='add-review'),
    path('review/<int:review_id>/delete', delete_review, name='delete-review')
]
