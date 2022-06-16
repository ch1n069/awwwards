from django.test import TestCase
from .models import *

# Create your tests here.


class RatingTestClass(TestCase):

    # setup method
    def setUp(self):
        self.bruno  = Rating(user='bruno',project="the buildwebsite", design_rate='4', userbilty_rate='3', content_rate='1')



    def test_instance(self):
        self.assertTrue(isinstance(self.bruno, Rating))


class Project(TestCase):


    def setUp(self):
        self.john = Project(user='john', title='the move us website',description='this is a webiste about a moving company', image="image.jpg", location="nairobi")


        self.assertTrue(isinstance(self.john, Project))



        
