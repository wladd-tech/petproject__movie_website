from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render
from main.models import Country, Movie
from django.db.models import Count

# def index(request):
#     movies = Movie.objects.all()

#     page = request.GET.get("page", 1)
#     paginator = Paginator(movies, 18)
#     current_page = paginator.page(page)

#     context = {
#         "movies": current_page,
#     }
#     return render(request, "main/main_page.html", context)


def index(request):
    foreign_movies = Movie.objects.prefetch_related('countries').exclude(countries__name='Россия')[:6]
    russian_movies = Movie.objects.prefetch_related('countries').filter(countries__name='Россия')[:6]
    watch_now = Movie.objects.order_by("-year")[:6]
    oldschool_movies = Movie.objects.order_by("year")[:6]

    context = {
        "movie_row_1": watch_now,
        "movie_row_2": foreign_movies,
        "movie_row_3": russian_movies,
        "movie_row_4": oldschool_movies,
    }
    return render(request, "main/main_page.html", context)


def catalog(request):
    if request.method == 'GET':
        movie_list = Movie.objects.prefetch_related("countries").order_by("year")
    elif request.method == 'POST':

        if request.POST.get("country") == "all":
            movie_list = Movie.objects.prefetch_related("countries")
        else:
            country_code = request.POST.get("country")
            movie_list = (Movie.objects.prefetch_related("countries")
                               .filter(countries__code=country_code))

            print(request.POST.get("country"))

    else:
        movie_list = None

    context = {
        "movie_list": movie_list,
        "country_list": Country.objects.all().only("code", "name"),
    }

    return render(request, "main/catalog_page.html", context)


def users(request):
    return render(request, "main/users_page.html")


def details(request, movie_id):
    movie = Movie.objects.prefetch_related('countries').get(id=movie_id)
    context = {
        "movie": movie,
    }
    return render(request, "main/detail_page.html", context)


def custom_404(request, exception):
    return render(request, "main/page_404.html")
