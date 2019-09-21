from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'career'

urlpatterns = [


    path('', views.index),
    url(r'^(?P<slug>[\w-]+)/$', views.vacancy_details, name='details')


]

