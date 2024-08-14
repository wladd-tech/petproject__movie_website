from django.http import JsonResponse
from django.shortcuts import render

# def index(request):
#     return JsonResponse({'data': 'Hello World!'})

def index(request):
    return render(request, 'main/index.html')


def catalog(request):
    return render(request, 'main/catalog.html')


def search(request):
    return render(request, 'main/search.html')


def users(request):
    return render(request, 'main/users.html')