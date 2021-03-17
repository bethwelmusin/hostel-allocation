from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            
            if not user:
                raise forms.ValidationError("User Does Not Exits")
            if not user.check_password(password):
                raise forms.ValidationError("Password incorrect")
            if not user.is_active:
                raise forms.ValidationError("user Not Active")
            
        return super(UserLoginForm, self).clean(*args, **kwargs)