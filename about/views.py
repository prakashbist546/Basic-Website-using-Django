from django.shortcuts import render
from .models import TeamMember
from .models import PhotoGallery


def index(request):
    team_members = TeamMember.objects.all().order_by('date')
    photo_gallery = PhotoGallery.objects.all()
    return render(request, '../templates/about/about_index.html', {'team_members': team_members, 'photo_gallery': photo_gallery})

