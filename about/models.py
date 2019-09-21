from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(default='default.png', blank=True)
    title = models.CharField(max_length=50)
    linkedin = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # return name of team member while querying
        return self.name


class PhotoGallery(models.Model):
    photo = models.ImageField()
    title = models.CharField(default='myphoto', max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
