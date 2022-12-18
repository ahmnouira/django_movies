from django.db import models

# Create your models here.


class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    # to improve readability in Admin
    # __str__ represents the class objects as a string
    def __str__(self) -> str:
        return self.headline
