from django import forms 
from award.models  import Project , Rating
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':"",
            'name':"username",
            'id':"username",
            'type':"text",
            'class':"form-control",
            'placeholder':"john doe",
            })
        self.fields['password1'].widget.attrs.update({
            'required':"",
            'name':"password1",
            'id':"password1",
            'type':"password",
            'class':"form-control",
            'placeholder':"password",
            })
        self.fields['password2'].widget.attrs.update({
            'required':"",
            'name':"password2",
            'id':"password2",
            'type':"password",
            'class':"form-control",
            'placeholder':"password",
            })
            


    class Meta:
        model = User
        fields = ['username','password1', 'password2']




class PostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'url']



class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating 
        fields = ['design_rate', 'userbility_rate', 'content_rate']
        