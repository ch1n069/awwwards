from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
from django.views.generic import ListView , CreateView , DetailView
from award.models import *
from award.forms import PostForm , SignUpForm , RatingForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import ProfileSerializer




from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm



# sserializing the profile model is

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all().order_by('user')
#     serializer_class = ProfileSerializer




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

#project details 
def project_details(request,post_id):

    project = Project.objects.filter(id=post_id)


    rating = Rating.objects.filter(id=project)




    if request.method == 'POST':

        project = Project.objects.get(id=post_id)



        user = request.user
     
        print(request.POST.get('design'))
        print(request.POST.get('usability'))
        print(request.POST.get('content'))

        design = request.POST.get('design')
        userbility = request.POST.get('usability')
        content = request.POST.get('content')


        new_rate = Rating(user=user, Project=project,design_rate=design, userbility_rate=userbility, content_rate=content)

        new_rate.save()
        # Rating.objects.create(
        #     Project=project,
        #     user = user,
        #     design_rate=design,
        #     userbility_rate=userbility,
        #     content_rate = content,
            # avg_rate=round((float(design_rate)+float(userbility_rate)+float(content_rate))/3,2),
        # )



        # avg = float(int(design) + int(usabilty)  + int(content) )/3
        # print(avg)

        # all = Rating(design_rate=design,userbility_rate=usabilty, content_rate=content, avg_rate=avg , Project=project, user=user)

        # all.save()

        # print(int(avg))
        print(project)

        return render(request, 'award/project.html',{"project":project})
    return render(request, 'award/project.html',{"rating":rating})



def Vote(request, id):
    if request.method == 'POST':

        project = Project.objects.get(id=id)
        current_user = request.user

        design_rate= request.POST["design"]
        userbility_rate = request.POST["userbility"]
        content_rate = request.POST["content"]


        Rating.objects.create(
            project=project,
            user = current_user,
            design_rate=design_rate,
            userbility_rate=userbility_rate,
            content_rate = content_rate,
            avg_rate=round((float(design_rate)+float(userbility_rate)+float(content_rate))/3,2),
        )

        avg_rating = (int(design_rate)+ int(userbility_rate)+ int(content_rate))/3


        project.rate=avg_rating 
        project.update_project()

        return render(request, "award/vote.html", {"success":"project rated successfully","project":project, "rating":Rating.objects.filter(project)})
    else:
        project = Project.object.get(id=id)
        return render(request, "award/vote.html",{"danger": "Project Rating Failed", "project": project})




   
        





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


def search_projects(request):


    if request.method == 'POST':
        term = request.POST['searched']
        # titles = Project.objects.filter(name__icontains=searched)
        print(term)

        return render(request, 'award/search.html',{'term':term})
    else:





        return render(request, 'award/search.html')