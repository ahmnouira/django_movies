from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    # string field for small to large sized strings
    # max_length argument is required
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="movies/images")

    # blank: mean that this field is optional
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):

    text = models.CharField(max_length=100)
    watch_again = models.BooleanField()
    # when someone creates  this object, the current datetime will be automatically filled in
    # note this makes the field non-editable, once the datetime is set, it is fixed
    # auto-populated
    date = models.DateTimeField(auto_now_add=True)
    # a user can create multiple reviews, a movie similarly **can have** similarly review
    # for user, the reference is to build-in user model that Django provides for authentication
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text
