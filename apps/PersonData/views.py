from django.shortcuts import render, HttpResponse

from .person_data import person_list

# Create your views here.

def read_person_data(request):
    context = {"persons" : person_list}
    return render(request,"list.html",context)