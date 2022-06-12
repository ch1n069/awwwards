from django.urls import path
from award import views

urlpatterns = [
    # path('', views.Home, name='home'),
    path('' , views.Home.as_view(), name='home'),
]