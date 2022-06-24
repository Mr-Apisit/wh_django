from django.shortcuts import render, HttpResponse

from .person_data import person_list

# Create your views here.

def read_person_data(request):
    # list_name = []
    # for person in person_list:
    #     list_name.append(person["full_name"])
    context = {"persons" : person_list}
    return render(request,"list.html",context)