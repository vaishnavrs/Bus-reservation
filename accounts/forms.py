from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'firstname'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'


class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username',}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))