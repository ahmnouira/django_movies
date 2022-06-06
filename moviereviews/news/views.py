from django.http import HttpRequest
from django.shortcuts import render
from .models import News

# Create your views here.


def news(request: HttpRequest):
    # most recent news
    data = News.objects.all().order_by('-date')
    return render(request, "news.html", {'data': data})
