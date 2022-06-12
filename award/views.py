from django.shortcuts import render
from django.contrib.auth import login, authenticate

# Create your views here.



def Home(request):
    return render(request, 'award/home.html')