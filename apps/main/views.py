from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from main.models import Movie

# def index(request):
#     return JsonResponse({'data': 'Hello World!'})


def index(request):
    movies = Movie.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(movies, 2)
    current_page = paginator.page(page)

    context = {
        "movies": current_page,
    }


    return render(request, "main/index.html", context)


def catalog(request):
    return render(request, "main/catalog.html")


def search(request):
    return render(request, "main/search.html")


def users(request):
    return render(request, "main/users.html")


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        "movie": movie,
    }
    return render(request, "main/details.html", context)


def page_not_found(request, exception):
    return render(request, "main/page404.html", status=404)
