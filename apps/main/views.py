from django.http import JsonResponse
from django.shortcuts import render
from main.models import Movie

# def index(request):
#     return JsonResponse({'data': 'Hello World!'})

def index(request):
    movies = Movie.objects.all()
    print(movies)
    context = {
        'movies': movies,
    }
    return render(request, 'main/index.html', context)


def catalog(request):
    return render(request, 'main/catalog.html')


def search(request):
    return render(request, 'main/search.html')


def users(request):
    return render(request, 'main/users.html')