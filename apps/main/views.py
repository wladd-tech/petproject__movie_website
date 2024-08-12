from django.http import JsonResponse
from django.shortcuts import render

# def index(request):
#     return JsonResponse({'data': 'Hello World!'})

def index(request):
    return render(request, 'main/index.html')