from django.urls import path 
from award import views

urlpatterns = [
    # path('', views.Home, name='home'),
    path('' , views.Home.as_view(), name="home"),
    path('signup/' , views.signup, name="register"),
    path('post/' , views.CreatePostView.as_view(), name="add_post"),


]