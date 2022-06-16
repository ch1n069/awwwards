from django.urls import path , include
from rest_framework import routers

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


#wiring up of our api 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))




]



# router = routers.DefaultRouter()
# router.register(path('profile/', views.ProfileViewSet))



