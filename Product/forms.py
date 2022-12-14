from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Contacto, Posteo

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña' , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        help_texts = {k:"" for k in fields}

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class PostForm(forms.ModelForm):

    class Meta:
        model = Posteo
        fields = '__all__'

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label='Contraseña' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña' , widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2', 'last_name' , 'first_name']
        help_texts = {k:"" for k in fields}
