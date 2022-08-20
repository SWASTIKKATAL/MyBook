#Creating a form
from django import forms
from .models import Users

class UserForm(forms.ModelForm):

    #create meta class
    class Meta:
        # specify model to be used
        model = Users

        fields = ["Username","Password"]