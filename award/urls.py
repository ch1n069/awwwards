from django.urls import path 
from award import views

urlpatterns = [
    # path('', views.Home, name='home'),
    path('' , views.Home.as_view(), name="home"),
    path('signup/' , views.signup, name="register"),
    path('post/' , views.CreatePostView.as_view(), name="add_post"),
    path('vote/' , views.Vote, name="vote"),
    path('project/<int:post_id>/' , views.project_details, name="project_details"),

    path('profile/', views.Profiles, name="profile"),
    path('search_projects/', views.search_projects, name="search-projects"),




]