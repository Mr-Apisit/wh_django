from django.urls import path
from .views import read_person_data

urlpatterns = [
    path('data/', read_person_data),
]