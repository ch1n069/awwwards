from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = 'award/home.html'

# def Home(request):
#     return render(request, 'award/home.html')