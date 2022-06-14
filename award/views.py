from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
from django.views.generic import ListView , CreateView , DetailView
from award.models import Project , Rating , Profile
from award.forms import PostForm , SignUpForm , RatingForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required



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




def Vote(request):
    form = RatingForm()
    if request.POST():
        form_valid = RatingForm.is_valid()
        if form_valid:
            form_validated = form_valid.save(commit=False)





    return render (request, 'award/vote.html' , {'form':form})


# profile view
@login_required
def Profiles(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first() 
    project  = Project.objects.filter(user_id=current_user.id).all() 

    ctx = {
        "profile":profile,
        "images":project

    }




    return render (request, 'award/profile.html', ctx) 