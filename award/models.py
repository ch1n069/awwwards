from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField() 
    url = models.URLField(blank=True)
    image = models.ImageField(null=True, upload_to="images")
    date = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.title 
