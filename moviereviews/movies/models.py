from django.db import models

# Create your models here.
class Movie(models.Model): 
    # string field for small to large sized strings
    # max_length argument is required
    title: models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image  = models.ImageField(upload_to="movies/images")

    # blank: mean that this field is optional
    url = models.URLField(blank=True)