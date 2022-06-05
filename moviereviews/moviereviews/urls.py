"""moviereviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from movies import views as movieViews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.home, name="home"), 
    # "about" Page not found (404)
    path("about/", movieViews.about, name='about'), 
    path("contact", movieViews.contact, name="contact"),
    path("signup", movieViews.signup, name="signup"), 
    
    # will forward any requests with "news" to news apps urls.py
    path("news/", include("news.urls")),
    # will forward any requests with 'movie/' to movie apps urls.py
    path("movie/", include('movies.urls'))
]



# to enable the sever serve the stored images, serve the static media from Django
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
