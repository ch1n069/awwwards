from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
from django.views.generic import ListView , CreateView , DetailView
from award.models import Project
from award.forms import PostForm , SignUpForm
from django.urls import reverse


from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class Home(ListView):
    model = Project


    template_name = 'award/home.html'

    success_url = reverse_lazy('home')

    

# def Home(request):
#     return render(request, 'award/home.html')



# creating posts
class CreatePostView(CreateView):
    model = Project 

    


    template_name = "award/post.html"
    fields = '__all__'





def signup(request):
    

    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = SignUpForm( )
        




    return render(request, 'registration/signup.html', {'form':form})