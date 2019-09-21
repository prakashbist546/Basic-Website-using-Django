from django.shortcuts import render


def index(request):
    return render(request, '../templates/home/home_index.html')
