from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class Home(TemplateView):


    template_name = 'award/home.html'

    success_url = reverse_lazy('award:home')

    

# def Home(request):
#     return render(request, 'award/home.html')


def signup(request):
    

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        




    return render(request, 'registration/signup.html', {'form':form})