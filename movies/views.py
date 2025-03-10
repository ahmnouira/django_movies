from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm
from .models import Movie, Review

# Create your views here.


def home(request: HttpRequest):
    searchTerm = request.GET.get("s")
    print("term:", searchTerm)
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, "home.html", {"term": searchTerm, "movies": movies})


def about(request: HttpRequest):
    return render(request, "about.html", {"name": "Ahmed Nouira", "page_name": "About"})


def contact(request: HttpRequest):
    return HttpResponse('<h3 style="color:green;">Welcome to Contact Page</h3>')


def mailing(request: HttpRequest):
    email = request.GET.get("email")
    return render(request, "mailing.html", {"email": email})


def details(request: HttpRequest, movie_id: int):
    movie = get_object_or_404(Movie, pk=movie_id)
    # retrieve reviews for a particular movie only
    reviews = Review.objects.filter(movie=movie)
    return render(request, "details.html", {"movie": movie, "reviews": reviews})


@login_required
def add_review(request: HttpRequest, movie_id):

    # get the movie object from the database
    movie = get_object_or_404(Movie, pk=movie_id)

    # it means that a user is navigating to the create review
    if request.method == "GET":
        return render(
            request, "add-review.html", {"form": ReviewForm(), "movie": movie}
        )

    else:
        try:
            form = ReviewForm(request.POST)
            # commit=False: because we want to specify the user and movie relationship for the review
            review: Review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect("details", review.movie.id)
        except ValueError:
            return render(
                request,
                "add-review.html",
                {"form": ReviewForm(), "error": "bad data passed in"},
            )


@login_required
def delete_review(request: HttpRequest, review_id: int):
    review: Review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect("details", review.movie.id)


@login_required
def edit_review(request: HttpRequest, review_id: int):

    # we supply the logged-in user to ensure that other users cant access the review if they manually enter the url path in the browser
    # only the who created this review can update/delete it
    review: Review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == "GET":
        form = ReviewForm(instance=review)
        return render(request, "edit-review.html", {"review": review, "form": form})

    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect("details", review.movie.id)
        except ValueError:
            return render(
                request,
                "edit-review.html",
                {"review": review, "form": form, "error": "Bad data in form"},
            )
