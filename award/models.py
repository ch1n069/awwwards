from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.urls import reverse

# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField() 
    url = models.URLField(blank=True)
    image = models.ImageField(null=True, upload_to="images")
    location = models.CharField(max_length=100, default="Kenya")
    date = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.title 



    def get_absolute_url(self):
        return reverse('home', )




# rating models

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_rate = models.IntegerField(default=0, null=True, blank=True)
    userbility_rate = models.IntegerField(default=0, null=True, blank=True) 
    content_rate = models.IntegerField(default=0, null=True, blank=True)
    avg_rate = models.IntegerField(default=0, null=True, blank=True)


