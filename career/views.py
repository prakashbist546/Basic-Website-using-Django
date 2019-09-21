from django.shortcuts import render
from .models import Vacancy


def index(request):

    vacancies = Vacancy.objects.all().order_by('date')
    return render(request, '../templates/career/career_index.html', {'vacancies': vacancies})


def vacancy_details(request, slug):
    vacancy = Vacancy.objects.get(slug=slug)
    return render(request, '../templates/career/vacancy_details.html', {'vacancy': vacancy})
