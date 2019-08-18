from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Theme, Tube


class TubeForm(forms.ModelForm):
    class Meta:
        model = Tube
        fields = ('name', 'link', 'description', 'theme') 

    def __init__(self, *args, **kwargs):
        super(TubeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control','placeholder':'type name tube'}
        self.fields['link'].widget.attrs = {'class': 'form-control','placeholder':'type the link youtube'}
        self.fields['description'].widget.attrs = {'class': 'form-control','rows': 3, 'cols': 40, 'style':'resize:none','placeholder':'description option'}
        self.fields['theme'].widget.attrs = {'class': 'form-control'}

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ('name',) 

    def __init__(self, *args, **kwargs):
        super(ThemeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control','placeholder':'type name theme'}

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'type your name'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'type your password'}))


class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput, max_length=100)
    password2 = forms.CharField(label='Confirme Password',widget=forms.PasswordInput, max_length=100)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control','placeholder':'type your name'}
        self.fields['password'].widget.attrs = {'class': 'form-control','placeholder':'type your password'}
        self.fields['password2'].widget.attrs = {'class': 'form-control','placeholder':'Repeat the Password'}