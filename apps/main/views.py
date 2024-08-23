from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render
from main.models import Movie


def index(request):
    movies = Movie.objects.all()

    page = request.GET.get("page", 1)
    paginator = Paginator(movies, 18)
    current_page = paginator.page(page)

    context = {
        "movies": current_page,
    }
    return render(request, "main/main_page.html", context)


def catalog(request):
    return render(request, "main/catalog_page.html")


def search(request):
    return render(request, "main/search_page.html")


def users(request):
    return render(request, "main/users_page.html")


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        "movie": movie,
    }
    return render(request, "main/detail_page.html", context)


def custom_404(request, exception):
    return render(request, "main/page_404.html")
